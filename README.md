![streetsquad](https://github.com/grupo-projeto-final-m5/api_images/blob/main/img/PROJETO_FINAL/logo/newlogo-removebg-preview-removebg-preview.png)

# BEM VINDO A STREET SQUAD API RESTFULL

API pensada e desenvolvida como projeto de finalização de modulo na kenzie academy brasil

Uma API com modelo de E-commerce para compra e vendas de roupas, permite a interação entre vendedores e compradores
Cria uma relação múltipla entre usuários e produtos considerando seus gostos e utilidades.


# DIAGRAMAS
### MVP
Em sua MVP temos o seguinte diagrama:

![diagrama mvp](https://github.com/grupo-projeto-final-m5/api_images/blob/main/img/PROJETO_FINAL/diagramas/diagramaMVP.png)

### DER
Como diagrama de entidade e relacionamentos temos o seguinte diagrama com suas entidades, atributos e propriedades, desenvolvida com 3 níveis de acesso:

![diagra de entidades de relacionamestos](https://github.com/grupo-projeto-final-m5/api_images/blob/main/img/PROJETO_FINAL/diagramas/derfinal.png)


## TIPOS DE USUARIOS E NIVEIS DE ACESSO

Foram utilizados 4 níveis de acessos a API com diferentes respostas e funcionalidades a cada uma.

 - Usuarios sem cadastro
 - Usuários cadastrados
 - vendedores
 - Administrador

### Usuários sem cadastro

 - visualiza produtos
 - se cadastra na plataforma

### Usuários cadastrado

 - Visualiza produtos
 - Adiciona produtos o seu carrinho de compras
 - Realiza pedidos com os produtos do carrinho
 - Visualiza todos os seus pedidos
 - Pode se tornar vendedor 

### Vendedor

 - Cadastra produtos na API.
 - Atualiza ou deleta produtos da API.
 - Visualiza todos os seus produtos.
 - visualiza todos os pedidos recebidos.
 - Atualiza os produtos do seu cadastro.
 - Tem acesso a todas as funções de compras da API.

### Administrador

 - Tem acesso integral as rotas da API.
 - pode cadastra, atualizar ou deletar qualquer usuário da API.
 - Pode atualizar ou deletar qualquer produto da API.
 - Tem acesso a todas as funções de compras da API.

## ROTAS

Todas as rotas do aplicativo estao descritas a baixo com seus verbos de acesso, endpoints e niveis de permissoes

### LOGIN
![rotas login](https://github.com/grupo-projeto-final-m5/api_images/blob/main/img/PROJETO_FINAL/rotas/rota_login.png)

### USUARIOS
![ROTAS USUARIOS](https://github.com/grupo-projeto-final-m5/api_images/blob/main/img/PROJETO_FINAL/rotas/rotas_usuarios.png)

### ENDEREÇOS
![ROTAS ENDERECOS](https://github.com/grupo-projeto-final-m5/api_images/blob/main/img/PROJETO_FINAL/rotas/rotas_enderecos.png)
### PRODUTOS
![ROTAS PRODUTOS](https://github.com/grupo-projeto-final-m5/api_images/blob/main/img/PROJETO_FINAL/rotas/rotas_produtos.png)
### CARRINHO DE COMPRAS
![ROTAS CARRINHOS](https://github.com/grupo-projeto-final-m5/api_images/blob/main/img/PROJETO_FINAL/rotas/rota_cart.png)
### PEDIDOS
![enter image description here](https://github.com/grupo-projeto-final-m5/api_images/blob/main/img/PROJETO_FINAL/rotas/rota_pedidos.png)
## TECNOLOGIAS UTILIZADAS

 - PYTHON
 - DJANGO
 - POSTGRESQL
 - GIT
 - GITHUB
 - RENDER
 - JIRA
 - SLACK
 - DIAGRAMS.NET

## CONCLUINDO
Nesta apresentação, exploramos os principais tópicos relacionados ao desenvolvimento de uma API para sustentar uma plataforma de e-commerce com diferentes níveis de acesso. O objetivo central desse projeto foi criar um ambiente funcional que atendesse às necessidades dos usuários e garantisse uma experiência fluida e eficiente.

Iniciamos com a definição do Produto Mínimo Viável (MVP), estabelecendo as funcionalidades essenciais para o lançamento inicial da plataforma. Em seguida, discutimos o Diagrama de Entidade e Relacionamento Conceitual, fornecendo uma visão clara da estrutura de dados e suas interações.

Destacamos a importância da gestão de produtos, com recursos como a busca por nome, categoria e ID, bem como a administração do estoque. Implementamos também um sistema que indica a indisponibilidade de produtos quando o estoque atinge zero unidades e tratamos os casos em que um produto indisponível está no carrinho de um usuário, retornando um erro apropriado.

Para facilitar a jornada de compra, desenvolvemos um carrinho de compras robusto, permitindo que os usuários selecionem produtos antes de finalizar a compra. Garantimos que o pedido só possa ser concluído se houver estoque suficiente e, caso os produtos provenham de diferentes vendedores, criamos um pedido separado para cada vendedor.

Acompanhando o ciclo do pedido, estabelecemos um sistema de status (Pedido Realizado, Em Andamento, Entregue) e configuramos o envio de e-mails ao comprador sempre que houver uma atualização. O pedido contém informações detalhadas dos produtos adquiridos, excluindo a quantidade em estoque, e permite que o vendedor atualize o status conforme necessário. Além disso, registramos o horário em que o pedido foi realizado, fornecendo transparência e rastreabilidade.

Para aprimorar a experiência do usuário, implementamos o relacionamento entre o usuário e seu endereço, simplificando a gestão de informações de entrega.

Por fim, abordamos o aspecto dos usuários, com a possibilidade de cadastro de diferentes tipos: Administrador, Vendedor e Cliente. O administrador tem acesso completo a todas as funcionalidades, incluindo a capacidade de transformar usuários comuns em vendedores. Os vendedores podem cadastrar novos produtos, atualizar o estoque, verificar pedidos realizados e visualizar todos os pedidos vendidos. Os clientes têm a flexibilidade de atualizar seu perfil para se tornarem vendedores, adicionar produtos ao carrinho e finalizar a compra. Além disso, oferecemos acesso limitado a usuários não autenticados para visualizar informações sobre os produtos.

Em suma, a API desenvolvida para essa plataforma de e-commerce proporciona uma base sólida para a construção de um ambiente dinâmico e funcional. Ela atende às necessidades dos usuários, oferecendo recursos abrangentes para gestão de produtos, carrinho de compras, pedidos e usuários, além de garantir uma experiência segura e eficiente. Estamos confiantes de que essa API é uma solução robusta para impulsionar o sucesso do seu negócio de e-commerce.

# EQUIPE DESENVOLVEDORA

## ANDRÉ LUIZ CAVALCANTE
![foto andre luiz cavalcante](https://github.com/grupo-projeto-final-m5/api_images/blob/main/img/PROJETO_FINAL/EQUIPE/ANDRE.png)
#### links de contato
 1. [Linkedin](https://www.linkedin.com/in/andr%C3%A9-luiz-cavalcante/)
 2.  [Git-hub](https://github.com/andrzcavalcante)

## JOSÉ GABRIEL
![jose Gabriel](https://github.com/grupo-projeto-final-m5/api_images/blob/main/img/PROJETO_FINAL/EQUIPE/GABRIEL.png)
#### links de contato
1. [Linkedin](https://www.linkedin.com/in/jos%C3%A9gabrielsouza/)
2. [Git-hub](https://github.com/Gabriieu)

## LUCCA CRUZ
![lucca cruz](https://github.com/grupo-projeto-final-m5/api_images/blob/main/img/PROJETO_FINAL/EQUIPE/LUCAS.jpg)
#### links de contato
1. [Linkedin](https://www.linkedin.com/in/luccaseabracruz/)
2. [Git-hub](https://github.com/luccaseabra)

## WELLINGTON EUGENIO DE PAULA
![wellinton eugenio ](https://github.com/grupo-projeto-final-m5/api_images/blob/main/img/PROJETO_FINAL/EQUIPE/WELLINGTON.jpeg)
#### links de contato
1. [Linkedin](https://www.linkedin.com/in/wellington-depaula/)
2. [Git-hub](https://github.com/wellinton-eugenio)

## AGRADECIMETOS

Gostaríamos de expressar nossa profunda gratidão à Kenzie  Academy Brasil, seus instrutores e monitores, por sua valiosa contribuição e suporte durante o desenvolvimento deste projeto.

Em primeiro lugar, gostaríamos de agradecer à Kenzie  Academy Brasil por fornecer uma plataforma excepcional de aprendizado e nos equipar com as habilidades necessárias para enfrentar desafios complexos, como a criação desta API para uma plataforma de e-commerce. A qualidade do ensino e o ambiente de aprendizado estimulante foram fundamentais para o nosso sucesso.

Também queremos expressar nosso sincero agradecimento aos instrutores Lucira Silva, Alexandre Alves e Pedro Hasler. Sua expertise, orientação e dedicação foram fundamentais ao longo do projeto. Suas habilidades técnicas, vontade de compartilhar conhecimento e capacidade de motivar e inspirar os alunos foram inestimáveis. Somos imensamente gratos pela oportunidade de aprender com profissionais tão talentosos e experientes.

Não podemos deixar de mencionar o corpo de monitores do módulo M5, cujo suporte e assistência foram inestimáveis. Suas orientações, esclarecimento de dúvidas e feedback foram cruciais para o nosso progresso e aprimoramento contínuo. Agradecemos por sua disponibilidade e paciência em nos ajudar a superar os desafios encontrados ao longo do projeto.

Estamos extremamente felizes em concluir este projeto e celebrar os resultados alcançados. Trabalhar juntos como um grupo coeso e dedicado nos trouxe uma grande satisfação e senso de realização. Estamos orgulhosos do nosso trabalho e das conquistas que alcançamos ao criar uma API funcional e robusta para suportar uma plataforma de e-commerce.

Mais uma vez, gostaríamos de agradecer à Kenzie  Academy Brasil, aos instrutores Lucira Silva, Alexandre Alves e Pedro Hasler, e ao corpo de monitores do módulo M5. Sua orientação, apoio e comprometimento foram fundamentais para o sucesso deste projeto. Estamos ansiosos para aplicar os conhecimentos adquiridos e continuar crescendo como profissionais na área de desenvolvimento de software.

Atenciosamente, EQUIPE G28 : ANDRE LUIZ CAVALCANTE, JOSÉ GABRIEL, LUCCA CRUZ E WELLINGTON EUGENIO
