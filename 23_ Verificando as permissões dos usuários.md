# Verificando as permissões dos usuários

##
```sh
SELECT CONCAT(QUOTE(user),'@',QUOTE(host)) UserAccount FROM mysql.user;  (LISTANDO USERS)

CREATE USER 'teste'@'localhost';

GRANT privileges ON scope TO conta;

SHOW GRANTS FOR 'root'@'localhost';

CREATE USER 'teste'@'localhost' IDENTIFIED BY '123456';

SELECT CONCAT(QUOTE(user),'@',QUOTE(host)) UserAccount FROM mysql.user;

GRANT FILE ON *.* TO 'teste'@'localhost';
```

##
```sh
SHOW GRANTS FOR 'teste'@'localhost';

GRANT CREATE TEMPORARY TABLES, LOCK TABLES ON *.* TO 'teste'@'localhost';

GRANT ALL ON teste.* TO 'teste'@'localhost';

GRANT SELECT ON mysql.user TO 'teste'@'localhost';

GRANT SELECT(User,Host), UPDATE(password_expired) ON mysql.user TO 'teste'@'localhost';

REVOKE FILE ON *.* FROM 'teste'@'localhost';

REVOKE CREATE TEMPORARY TABLES, LOCK TABLES ON *.* FROM 'teste'@'localhost';

REVOKE ALL ON teste.* FROM 'teste'@'localhost';

REVOKE SELECT(User,Host), UPDATE(password_expired) ON mysql.user FROM 'teste'@'localhost';

REVOKE SELECT ON mysql.user FROM 'teste'@'localhost';

SHOW GRANTS FOR 'user1'@'localhost';

RENAME USER 'teste'@'localhost' TO 'teste2'@'localhost';

DROP USER 'teste'@'localhost';

-- Liks de ref:
--https://dev.mysql.com/doc/refman/8.0/en/grant.html
```
