## Disclaimer geral
Trata-se de uma prova de conceito realizando o **mínimo** necessário. Não há considerações sobre segurança nesta versão.

## Procedimentos mínimos para rodar
  * instalar as dependências;
  * preencher o `settings.conf` corretamente: pelo menos o `ALLOWED_HOSTS` e as informações do OAuthUSP;
  * criar e executar as migrations;
  * acessar o `/accounts/login` para criar a sua primeira conta com senha única;
  * rodar o admin.py para tornar essa conta administradora;
  * acessar o `/o/applications` para criar a chave de API.

### Informações testadas para a chave de API
  * client type: confidential;
  * authorization grant type: authorization code.
