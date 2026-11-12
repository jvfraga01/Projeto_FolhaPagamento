from functools import wraps

from flask import (Blueprint, abort, flash, g, redirect, render_template, request,
                   session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from .db import get_db
from .regras import senha_inicial

bp = Blueprint("auth", __name__)
HASH_FALSO = generate_password_hash("hash-para-tempo-constante")


# Só para esconder botões na tela. A proteção de verdade é o @nivel_exigido de cada rota.
PERMISSOES = {"colaborador.editar": {1}, "folha.gerar": {1}}


def pode(usuario, acao):
    return bool(usuario) and usuario["nivel_acesso"] in PERMISSOES[acao]


def login_obrigatorio(view):
    @wraps(view)
    def envelope(*args, **kwargs):
        if g.usuario is None:
            return redirect(url_for("auth.login"))
        return view(*args, **kwargs)
    return envelope


def nivel_exigido(*niveis):
    """Permissão verificada NO BACKEND: nível fora da lista recebe 403 e nenhum dado."""
    def decorador(view):
        @wraps(view)
        def envelope(*args, **kwargs):
            if g.usuario is None:
                return redirect(url_for("auth.login"))
            if g.usuario["nivel_acesso"] not in niveis:
                abort(403)
            return view(*args, **kwargs)
        return envelope
    return decorador


@bp.route("/login", methods=["GET", "POST"])
def login():
    if g.usuario:
        return redirect(url_for("inicio"))
    erro = None
    if request.method == "POST":
        matricula = request.form.get("matricula", "").strip()
        senha = request.form.get("senha", "")
        linha = None
        if matricula.isdigit() and len(matricula) <= 9:
            linha = get_db().execute(
                "SELECT matricula, senha_hash, status, data_nascimento FROM colaborador WHERE matricula = ?",
                (int(matricula),)).fetchone()
        senha_ok = check_password_hash(linha["senha_hash"] if linha else HASH_FALSO, senha)
        if linha and senha_ok and linha["status"] == "Ativo":
            session.clear()
            session["matricula"] = linha["matricula"]
            session.permanent = True
            # BUG002: quem entra com a senha inicial (data de nascimento) é obrigado a trocá-la.
            if senha == senha_inicial(linha["data_nascimento"]):
                session["trocar_senha"] = True
                return redirect(url_for("auth.trocar_senha"))
            return redirect(url_for("inicio"))
        erro = "Matrícula ou senha incorretos, ou usuário inativo."
    return render_template("login.html", erro=erro), (401 if erro else 200)


@bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("auth.login"))


@bp.route("/senha", methods=["GET", "POST"])
@login_obrigatorio
def trocar_senha():
    if request.method == "POST":
        atual = request.form.get("atual", "")
        nova = request.form.get("nova", "")
        confirma = request.form.get("confirma", "")
        db = get_db()
        linha = db.execute("SELECT senha_hash, data_nascimento FROM colaborador WHERE matricula = ?",
                           (g.usuario["matricula"],)).fetchone()
        if not check_password_hash(linha["senha_hash"], atual):
            flash("Senha atual incorreta.", "erro")
        elif len(nova) < 6:
            flash("A nova senha precisa ter pelo menos 6 caracteres.", "erro")
        elif nova == senha_inicial(linha["data_nascimento"]):
            flash("A nova senha não pode ser a senha inicial (data de nascimento).", "erro")
        elif nova != confirma:
            flash("A confirmação não confere com a nova senha.", "erro")
        else:
            db.execute("UPDATE colaborador SET senha_hash = ? WHERE matricula = ?",
                       (generate_password_hash(nova), g.usuario["matricula"]))
            db.commit()
            session.pop("trocar_senha", None)
            flash("Senha alterada com sucesso.", "ok")
            return redirect(url_for("inicio"))
    return render_template("senha.html")
