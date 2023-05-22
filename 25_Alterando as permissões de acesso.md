# Alterando as permissões de acesso

##
```sh
SELECT User, Host FROM mysql.user WHERE Host REGEXP '[%_]';

RENAME USER 'replication'@'%' TO 'replication'@'192.168.0.%';

RENAME USER 'replication'@'%' TO 'replication'@'hostMASTER.seudominio.com';

RENAME USER 'replication'@'%' TO 'replication'@'%.seudominio.com';
```
