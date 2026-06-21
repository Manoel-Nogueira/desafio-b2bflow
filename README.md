# Desafio b2bflow

Aplicação desenvolvida em Python para buscar contatos no Supabase e enviar mensagens personalizadas via Z-API.

## Setup da tabela no Supabase

Tabela: `users`

| Campo      | Tipo        |
| ---------- | ----------  |
| id         | bigint      |
| name       | varchar     |
| number     | varchar     |
| created_at | timestamptz |

Exemplo:

| id | name  | number        |
| -- | ----- | ------------- |
| 1  | João  | 5575999999999 |

> Desative o RLS no Supabase.
> O campo `number` deve estar no formato internacional contendo apenas números.

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# URL do projeto no Supabase
SUPABASE_URL=

# Chave de acesso ao Supabase
SUPABASE_KEY=

# ID da instância do Z-api
ZAPI_INSTANCE_ID=

# Token de acesso à instância do Z-api
ZAPI_INSTANCE_TOKEN=
```

## Como rodar

### 1. Criar o ambiente virtual

```bash
python -m venv venv
```

### 2. Ativar o ambiente virtual

Linux:

```bash
source venv/bin/activate
```

Windows (PowerShell):

```bash
.\venv\Scripts\Activate.ps1
```

Windows (CMD):

```bash
.\venv\Scripts\activate.bat
```
> Caso ocorra um erro de permissão, execute o seguinte comando: `Set-ExecutionPolicy Bypass -Scope Process` ou `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` e depois tente ativar o venv novamente.

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação

```bash
python src/main.py
```

## Funcionamento

1. Busca os contatos na tabela `users`.
2. Personaliza a mensagem utilizando o campo `name`.
3. Envia a mensagem via Z-API para o número armazenado em `number`.

Mensagem enviada:

```text
Olá, <nome_contato> tudo bem com você?
```

Developed by **Manoel Nogueira Melo Filho**
