BIBLIOTECA VIRTUAL IESGO

Este é um projeto de uma aplicação web simples desenvolvida com Django para gerenciar um catálogo de livros. O projeto envolve a criação de um modelo de dados, views, templates e URLs para a aplicação.

Tecnologias Utilizadas

- Django: Framework web em Python utilizado para o desenvolvimento da aplicação.
- HTML e CSS: Utilizados para criar a interface do usuário.
- SQLite: Banco de dados utilizado para armazenar os dados da aplicação durante o desenvolvimento.
- Git e GitHub: Sistema de controle de versão e plataforma de hospedagem de código utilizado para gerenciar o código-fonte do projeto.

Etapas do Projeto

1. Configuração do Ambiente Django:
   - Configuração do ambiente virtual e instalação do Django.
   - Criação de um novo projeto Django chamado book_manager.

2. Criação da Aplicação:
   - Criação de uma nova aplicação dentro do projeto chamada books.

3. Definição do Modelo de Dados:
   - No arquivo models.py da aplicação books, foi definido um modelo Book com os campos: Título, Autor e Data de Publicação.

4. Configuração do Admin:
   - O modelo Book foi registrado no admin do Django para gerenciamento através da interface administrativa.

5. Criação da View e Template:
   - No arquivo views.py, foi criada uma view para listar todos os livros cadastrados.
   - Criado um template HTML chamado book_list.html para exibir a lista de livros.

6. Configuração das URLs:
   - No arquivo urls.py da aplicação books, foi definida a rota para a view criada.
   - A aplicação books foi incluída nas URLs do projeto principal no arquivo urls.py do projeto.

7. Migrações do Banco de Dados:
   - Foram realizadas as migrações para criar as tabelas no banco de dados.

8. Criação de Superusuário e Execução do Servidor:
   - Foi criado um superusuário para acessar o admin do Django.
   - O servidor de desenvolvimento do Django foi executado.

9. Testando a Aplicação:
   - O admin do Django foi acessado em http://127.0.../admin e alguns livros foram adicionados.
   - A lista de livros foi acessada em http://127.0.../books para verificar a aplicação em ação.

Desafios Adicionais

Além das etapas básicas do projeto, foram realizados os seguintes desafios adicionais:

- Adicionados formulários para permitir a adição e edição de livros diretamente na aplicação (fora do admin).
- Estilizados os templates usando CSS para uma melhor apresentação visual.
- Implementada a paginação na lista de livros para facilitar a navegação.
- Permitida a visualização de todos os elementos do modelo dentro do admin, incluindo a capa do livro como uma foto.

Executando o Projeto

Para executar este projeto em seu ambiente local, siga as etapas abaixo:

1. Clone este repositório em sua máquina:
   git clone https://github.com/seu-usuario/biblioteca-virtual-iesgo.git

2. Navegue até o diretório do projeto:
   cd biblioteca-virtual-iesgo

3. Instale as dependências do Python listadas no arquivo requirements.txt:
   pip install -r requirements.txt

4. Execute as migrações do banco de dados:
   python manage.py migrate

5. Crie um superusuário para acessar o admin do Django:
   python manage.py createsuperuser

6. Inicie o servidor de desenvolvimento do Django:
   python manage.py runserver

7. Acesse o admin do Django em http://127.0.../admin para adicionar livros.
8. Acesse a lista de livros em http://127.0.../books para ver a aplicação em ação.
