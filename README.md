# Sales API

API RESTful de sistema de vendas desenvolvida com Django e Django REST Framework.

## 📋 Sobre o Projeto

Este projeto é um sistema de gerenciamento de vendas desenvolvido como parte dos estudos em Django REST Framework. A API permite gerenciar produtos, clientes, pedidos e métodos de pagamento, oferecendo uma solução completa para operações de vendas.

**Desenvolvedor:** Kaue  
**Tecnologias:** Django 6.0, Django REST Framework, SQLite, drf-spectacular

## 🚀 Funcionalidades

### Módulos Principais

- **Marcas (Brands)**: Gerenciamento de marcas de produtos
- **Categorias (Categories)**: Organização de produtos por categorias
- **Produtos (Products)**: Cadastro de produtos com controle de estoque
- **Clientes (Customers)**: Gestão de clientes físicos (PF) e jurídicos (PJ)
- **Métodos de Pagamento (Payment Method)**: Configuração de formas de pagamento com suporte a parcelamento
- **Pedidos (Orders)**: Sistema completo de pedidos com itens e parcelas

### Recursos Implementados

- ✅ CRUD completo para todos os módulos
- ✅ Sistema de pedidos com múltiplos itens
- ✅ Controle de estoque de produtos
- ✅ Suporte a clientes físicos e jurídicos
- ✅ Sistema de parcelamento de pedidos
- ✅ Documentação automática da API (Swagger/OpenAPI)
- ✅ Validações de negócio
- ✅ Signals para atualização automática de estoque

## 🛠️ Tecnologias Utilizadas

- **Django 6.0**: Framework web Python
- **Django REST Framework**: Construção de APIs REST
- **drf-spectacular**: Documentação automática da API
- **SQLite**: Banco de dados (desenvolvimento)
- **python-dotenv**: Gerenciamento de variáveis de ambiente

## 📦 Estrutura do Projeto

```
sales-api/
├── app/                    # Configurações principais do Django
│   ├── settings.py         # Configurações do projeto
│   └── urls.py            # URLs principais
├── brands/                 # Módulo de marcas
├── categories/            # Módulo de categorias
├── products/              # Módulo de produtos
├── customers/             # Módulo de clientes
├── payment_method/        # Módulo de métodos de pagamento
├── orders/                # Módulo de pedidos
│   └── signals.py        # Signals para atualização de estoque
└── docs/                  # Documentação da API
```

## 🗄️ Modelos de Dados

### Clientes
- **Client**: Cliente base (PF ou PJ)
- **PhysicalPerson**: Dados de pessoa física (CPF, nome completo, data de nascimento)
- **LegalPerson**: Dados de pessoa jurídica (CNPJ, razão social, nome fantasia)

### Produtos
- **Products**: Produtos com nome, categoria, marca, preço, estoque e controle de estoque

### Pedidos
- **Order**: Pedido com cliente, método de pagamento, valor total e status
- **OrderItem**: Itens do pedido com produto, quantidade e preços
- **InstallmentOrder**: Parcelas do pedido com número, valor, data de vencimento e status de pagamento

### Métodos de Pagamento
- **PaymentMethod**: Métodos de pagamento com suporte a parcelamento, juros e prazo

## 🔧 Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos para Instalação

1. **Clone o repositório** (ou navegue até o diretório do projeto)

2. **Crie um ambiente virtual** (recomendado):
```bash
python -m venv venv
```

3. **Ative o ambiente virtual**:
   - Windows:
   ```bash
   venv\Scripts\activate
   ```
   - Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

4. **Instale as dependências**:
```bash
pip install django djangorestframework drf-spectacular python-dotenv
```

5. **Configure as variáveis de ambiente**:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione a chave secreta:
   ```
   SECRET_KEY=sua-chave-secreta-aqui
   ```

6. **Execute as migrações**:
```bash
python manage.py migrate
```

7. **Crie um superusuário** (opcional, para acessar o admin):
```bash
python manage.py createsuperuser
```

8. **Inicie o servidor de desenvolvimento**:
```bash
python manage.py runserver
```

O servidor estará disponível em `http://127.0.0.1:8000/`

## 📚 Documentação da API

A documentação interativa da API está disponível através do drf-spectacular:

- **Swagger UI**: `http://127.0.0.1:8000/api/v1/schema/swagger-ui/`
- **ReDoc**: `http://127.0.0.1:8000/api/v1/schema/redoc/`
- **Schema OpenAPI**: `http://127.0.0.1:8000/api/v1/schema/`

## 🔌 Endpoints da API

### Base URL: `/api/v1/`

#### Marcas
- `GET /brands/` - Lista todas as marcas
- `POST /brands/` - Cria uma nova marca
- `GET /brands/{id}/` - Detalhes de uma marca
- `PUT/PATCH /brands/{id}/` - Atualiza uma marca
- `DELETE /brands/{id}/` - Remove uma marca

#### Categorias
- `GET /categories/` - Lista todas as categorias
- `POST /categories/` - Cria uma nova categoria
- `GET /categories/{id}/` - Detalhes de uma categoria
- `PUT/PATCH /categories/{id}/` - Atualiza uma categoria
- `DELETE /categories/{id}/` - Remove uma categoria

#### Produtos
- `GET /products/` - Lista todos os produtos
- `POST /products/` - Cria um novo produto
- `GET /products/{id}/` - Detalhes de um produto
- `PUT/PATCH /products/{id}/` - Atualiza um produto
- `DELETE /products/{id}/` - Remove um produto

#### Clientes
- `GET /customers/` - Lista todos os clientes
- `POST /customers/` - Cria um novo cliente
- `GET /customers/{id}/` - Detalhes de um cliente
- `PUT/PATCH /customers/{id}/` - Atualiza um cliente
- `DELETE /customers/{id}/` - Remove um cliente

#### Métodos de Pagamento
- `GET /payment_method/` - Lista todos os métodos de pagamento
- `POST /payment_method/` - Cria um novo método de pagamento
- `GET /payment_method/{id}/` - Detalhes de um método de pagamento
- `PUT/PATCH /payment_method/{id}/` - Atualiza um método de pagamento
- `DELETE /payment_method/{id}/` - Remove um método de pagamento

#### Pedidos
- `GET /orders/` - Lista todos os pedidos
- `POST /orders/` - Cria um novo pedido
- `GET /orders/{public_id}/` - Detalhes de um pedido
- `PUT/PATCH /orders/{public_id}/` - Atualiza um pedido
- `DELETE /orders/{public_id}/` - Remove um pedido

## 🔄 Funcionalidades Especiais

### Sistema de Pedidos

O sistema de pedidos inclui:
- Criação de pedidos com múltiplos itens
- Cálculo automático de valores totais
- Suporte a parcelamento
- Atualização automática de estoque via signals
- Status de pedidos (Realizada/Cancelada)

### Controle de Estoque

- Produtos podem ter controle de estoque habilitado/desabilitado
- Atualização automática do estoque ao criar pedidos
- Validação de estoque disponível

### Clientes

- Suporte a dois tipos de clientes:
  - **Pessoa Física (PF)**: CPF, nome completo, data de nascimento
  - **Pessoa Jurídica (PJ)**: CNPJ, razão social, nome fantasia
- Cliente especial "Consumidor Final" para vendas sem cadastro

## 📝 Próximas Melhorias

Conforme o arquivo `to-do.md`, as seguintes melhorias estão planejadas:

- [ ] Permitir múltiplas formas de pagamento por pedido
- [ ] Permitir envio do valor do produto em caso de desconto
- [ ] Implementar sistema de vendedores (em avaliação)

## 👨‍💻 Desenvolvedor

**Kaue**  
Estudante de Django REST Framework

Este projeto foi desenvolvido como parte dos estudos em desenvolvimento de APIs REST com Django.

## 📄 Licença

Este projeto é de uso educacional e foi desenvolvido para fins de aprendizado.

## 🤝 Contribuições

Este é um projeto de estudo pessoal. Sugestões e feedbacks são bem-vindos!

---

**Nota:** Este projeto está em desenvolvimento ativo e pode conter funcionalidades experimentais.

