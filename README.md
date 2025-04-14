# 🌌 Alura Space

O **Alura Space** é uma aplicação web desenvolvida com Django e Python, que permite aos usuários visualizar, adicionar, editar e excluir imagens relacionadas ao espaço, como estrelas, galáxias e nebulosas. O projeto foi desenvolvido como parte da formação em Django da Alura, com o objetivo de consolidar conhecimentos em desenvolvimento web com Django.

## 🚀 Funcionalidades

- Visualização de uma galeria de imagens do espaço.
- Cadastro de novas imagens com informações detalhadas.
- Edição e exclusão de imagens existentes.
- Filtragem de imagens por categoria.
- Pesquisa de imagens por nome.
- Autenticação de usuários com login e cadastro.
- Painel administrativo utilizando o Django Admin.

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- HTML5
- CSS3
- JavaScript
- Bootstrap 5

## 📦 Instalação e Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/moreira-m98/alura_space.git
   cd alura_space
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

6. Acesse a aplicação em [http://localhost:8000](http://localhost:8000)

## 📁 Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `apps/` - Contém os aplicativos Django da aplicação.
- `media/` - Armazena os arquivos de mídia, como as imagens carregadas.
- `static/` - Contém os arquivos estáticos, como CSS e JavaScript.
- `templates/` - Contém os templates HTML da aplicação.
- `manage.py` - Script de gerenciamento do Django.
- `requirements.txt` - Lista de dependências do projeto.

## 👤 Autor

Desenvolvido por [moreira-m98](https://github.com/moreira-m98) como parte do curso de Django da Alura.
