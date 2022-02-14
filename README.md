# Delivery API

## Cabeçalho

Autor: Gabriel Moretti de Souza

## Objetivos da aplicação

Desenvolvimento de uma aplicação CRUD com uma API simples, que possa:

* Cadastrar pedidos;
* Listar os pedidos cadastrados;
* Editar os pedidos cadastrados;
* Excluir um dos pedidos cadastrados.

## Processo de desenvolvimento

A aplicação será desenvolvida em linguagem Python3, fazendo uso do framework Flask (e seus auxiliares) para criá-la e auxiliar também no desenvolvimento da API.

**O sistema operacional utilizado foi o sistema Linux.**

Você pode conferir o desenvolvimento do projeto por meio da seção de _issues_ deste repositório, com suas respectivas tarefas por _issue_ e os comentários necessários. É possível encontrá-las neste [link](https://github.com/MorettiGS/delivery-api/issues?q=is%3Aissue+is%3Aclosed+sort%3Acreated-asc).

## Como executar a aplicação

Como pedido, a aplicação deverá ser armazenada em uma imagem Docker, esta que pode ser encontrada no link localizado na descrição do projeto, ou [aqui](https://hub.docker.com/repository/docker/morettigs27/delivery-api/tags?page=1&ordering=last_updated). Desta forma, também deve ser possível executar a aplicação em um container Docker.

### Utilizando Docker

Partindo do pressuposto que o usuário possui Docker em seu computador, você deverá primeiro encontrar, em seu terminal, o diretório do projeto, este podendo ser baixado após digitar o código existente no repositório Docker apresentado `docker pull morettigs27/delivery-api:app`. Após estar localizado no mesmo, deverá digitar o seguinte comando: `docker run -p 5000:5000 morettigs27/delivery-api:app`, isto deverá iniciar um novo container Docker na sua máquina.

Dessa forma, isso também iniciará a sua aplicação, retornando no terminal alguns dados relacionados ao estado da mesma. Esta aplicação, após iniciada, se encontrará na porta localhost:5000, ou seja, no link http://localhost:5000/. Para continuidade, verifique o tópico 'Ferramentas de teste'.

### Não utilizando Docker

Mesmo não fazendo parte dos requisitos do projeto, também é possível executar a aplicação sem fazer uso da imagem Docker, basta, se localizando no repositório do projeto (após ser baixado pelo GitHub), executar o seguinte comando em seu terminal: `python ./app/app.py`. Isso deverá iniciar sua aplicação na porta localhost:5000, ou seja, no link http://localhost:5000/. Para continuidade, verifique o tópico 'Ferramentas de teste'.

### Ferramentas de teste

Como esta aplicação se refere a uma API, para o teste das funções da mesma, poderá ser feito o uso de ferramentas como o [Postman](https://www.postman.com/) ou o [Insomnia](https://insomnia.rest/), os dois podendo ser respectivamente baixados nos links: [Download Postman](https://www.postman.com/downloads/), [Download Insomnia](https://insomnia.rest/download). Estas duas ferramentas podem garantir o funcionamento da aplicação.

Porém, caso essas não sejam ideais, ainda existem formas diferentes de se verificar a resposta da API. Além de pedidos encaminhados, incluindo o uso do [cURL](https://curl.se/), a forma mais simples de se realizar esse processo seria com a utilização do próprio site gerado pela aplicação. Dito isso, esta opção ainda é inviável, visto que os parâmetros necessários para a realização de alguns dos endpoints solicitados ainda não podem ser enviados pelo próprio site. Por um outro lado, a API em si e os endpoints que não fazem uso de parâmetros ainda funcionam corretamente pelo site.
