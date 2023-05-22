# Criando uma forte politica de senhas

##
```sh
SELECT @@plugin_dir;

vim /etc/mysql/mysql.conf.d/mysqld.cnf

[mysqld]
plugin-load-add=validate_password.so
plugin-load-add=adt_null.so

service mysql restart

mysql -u root -p

SHOW VARIABLES LIKE 'validate_password%';
```

##
```sh
vim /etc/mysql/mysql.conf.d/mysqld.cnf

[mysqld]
plugin-load-add=validate_password.so
validate_password_length=10
validate_password_mixed_case_count=1
validate_password_number_count=2
validate_password_special_char_count=1

service mysql restart
```

##
```sh
mysql -u replication -p

SHOW VARIABLES LIKE 'validate_password%';

SET PASSWORD = PASSWORD('weak-password');

SET PASSWORD = PASSWORD('Str0ng-Pa33w@rd');

SELECT VALIDATE_PASSWORD_STRENGTH('abc') ;

SELECT VALIDATE_PASSWORD_STRENGTH('senha-fraca');

SELECT VALIDATE_PASSWORD_STRENGTH('S3nhA-F88r%te');
```
