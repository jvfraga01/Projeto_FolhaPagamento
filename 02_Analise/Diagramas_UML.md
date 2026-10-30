# 4. Diagramas UML

## Diagrama de Classes (modelo de domínio)
As estratégias de cálculo são implementadas como funções registradas em `CALCULADORES` (módulo `regras.py`);
no diagrama aparecem como classes para representar o padrão **Strategy** (RNF004). Cada calculador segue as fórmulas do cliente; o regime opcional de metas é um parâmetro (`regime_metas`) recebido pelos calculadores, desligado por padrão.

```mermaid
classDiagram
    class Colaborador {
        +int matricula
        +String nome
        +Date dataNascimento
        +Date dataInicioContrato
        +Date dataFimContrato
        +int nivelAcesso
        +String status
        +String tipo
        +int salarioBaseCentavos
        +int percentualComissaoBp
        +int valorUnidadeCentavos
        +String senhaHash
        +desabilitar()
        +reativar()
    }
    class Periodo {
        +int ano
        +int mes
        +String status
        +fechar()
    }
    class Folha {
        +String nome
        +String tipo
        +int salarioBaseCentavos
        +int percentualComissaoBp
        +int valorUnidadeCentavos
        +int meta
        +int vendasCentavos
        +int quantidadeProduzida
        +boolean metaAtingida
        +int percentualAplicadoBp
        +int adicionaisCentavos
        +int totalCentavos
        +calcular()
    }
    class CalculoRemuneracao {
        <<interface>>
        +calcular(dados) Resultado
    }
    class CalculoPadrao
    class CalculoComissionado
    class CalculoProducao
    Colaborador "1" --> "*" Folha : possui
    Periodo "1" --> "*" Folha : contem
    Folha ..> CalculoRemuneracao : usa
    CalculoRemuneracao <|.. CalculoPadrao
    CalculoRemuneracao <|.. CalculoComissionado
    CalculoRemuneracao <|.. CalculoProducao
```

## Diagrama de Sequência – Cadastro de colaborador
Inclui o fluxo de sucesso e as rejeições previstas em UC001 (sem permissão e dado inválido).
```mermaid
sequenceDiagram
    actor RH as Administrador RH
    participant UI as Interface Web
    participant S as Sistema Flask
    participant R as Regras (regras.py)
    participant B as Banco SQLite
    RH->>UI: Preenche e confirma o cadastro
    UI->>S: POST colaboradores novo (com token CSRF)
    alt Token CSRF invalido
        S-->>UI: 400 Requisicao invalida
    else Usuario sem nivel 1
        S-->>UI: 403 Acesso negado, nada e gravado
    else Usuario nivel 1
        S->>R: Valida nome, datas, salario e dado do tipo
        alt Dado invalido (nome vazio, valor negativo, data invalida)
            R-->>S: Erros por campo
            S-->>UI: 400 Formulario com mensagens, nada e gravado
            UI-->>RH: Mostra os erros nos campos
        else Dados validos
            S->>B: INSERT colaborador com senha em hash
            B-->>S: Matricula gerada
            S-->>UI: Redireciona com mensagem de sucesso
            UI-->>RH: Lista com o novo colaborador
        end
    end
```

## Diagrama de Sequência – Geração, lançamento e fechamento da folha
Inclui as rejeições de UC003, UC010 e UC011. O cálculo usa as fórmulas do cliente; a definição de meta só ocorre no modo opcional com metas.
```mermaid
sequenceDiagram
    actor RH as Administrador RH
    participant S as Sistema Flask
    participant R as Regras de calculo
    participant B as Banco SQLite
    RH->>S: Gerar folha do mes (mes e ano)
    alt Usuario sem nivel 1
        S-->>RH: 403 Acesso negado
    else Mes ou ano invalido
        S-->>RH: Mensagem de erro, nada e gerado
    else Periodo ja FECHADO
        S-->>RH: Recusa informando que o mes esta fechado
    else Geracao valida
        S->>B: Busca colaboradores com contrato no mes
        loop Para cada colaborador sem folha no mes
            opt Modo opcional com metas
                S->>B: Busca folha do mes anterior
                S->>R: Define a meta do mes
            end
            S->>R: Calcula remuneracao (formulas do cliente)
            S->>B: INSERT folha
        end
        S-->>RH: Folha aberta com total
    end
    RH->>S: Lanca vendas e producao
    alt Mes FECHADO
        S-->>RH: 403 somente leitura
    else Valor negativo ou invalido
        S-->>RH: Mensagem de erro, nada e salvo
    else Valores validos
        S->>R: Recalcula cada folha
        S->>B: UPDATE folha
        S-->>RH: Lancamentos salvos
    end
    RH->>S: Fechar mes
    alt Mes ja fechado ou sem folhas
        S-->>RH: Mensagem de recusa
    else Mes aberto com folhas
        S->>B: UPDATE periodo para FECHADO
        S-->>RH: Folha congelada
    end
```

## Diagrama de Sequência – Acesso negado ao nível 3
```mermaid
sequenceDiagram
    actor C as Colaborador nivel 3
    participant S as Sistema Flask
    participant B as Banco SQLite
    C->>S: GET folha com id de outra pessoa
    S->>B: Busca a folha pelo id
    B-->>S: Folha de outro colaborador
    S->>S: Matricula da sessao difere da folha
    S-->>C: 403 Acesso negado sem dados
```

## Modelo de Dados (ER)
```mermaid
erDiagram
    COLABORADOR ||--o{ FOLHA : possui
    PERIODO ||--o{ FOLHA : contem
    COLABORADOR {
        int matricula PK
        string nome
        string data_nascimento
        string data_inicio_contrato
        string data_fim_contrato
        int nivel_acesso
        string status
        string senha_hash
        string tipo
        int salario_base_centavos
        int percentual_comissao_bp
        int valor_unidade_centavos
    }
    PERIODO {
        int id PK
        int ano
        int mes
        string status
    }
    FOLHA {
        int id PK
        int periodo_id FK
        int matricula FK
        int meta
        int vendas_centavos
        int quantidade_produzida
        int adicionais_centavos
        int total_centavos
    }
```

## Diagrama de Estados – Período da folha
```mermaid
stateDiagram-v2
    [*] --> ABERTO : gerar folha
    ABERTO --> ABERTO : lancar vendas e producao
    ABERTO --> FECHADO : fechar mes
    FECHADO --> [*]
```
