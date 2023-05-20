# Configurações após instalação

##
```sh
Após a instalação, devemos fazer as alterações de alterações de senhas do root, mudanças de seguranças, entre outras coisas. 
As alterações ficam em 

/etc/mysql/mysql.conf.d

no arquivo 

mysqld.cnf

E nele temos as configurações padrões que já vem após uma instalação.

vim /etc/mysql/mysql.conf.d/mysqld.cnf

[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
log-error       = /var/log/mysql/error.log
```

##
```sh
Temos muitas outras configurações disponiveis para se alterar

https://github.com/Mazuco/MySQL/blob/master/my.cnf

https://dev.mysql.com/doc/refman/8.0/en/option-files.html

Caso queria alterar a senha do Root, rode esse comando:

# mysqladmin -u root -p flush-privileges password "123456"

E depois faça os testes:

# mysql -h localhost -u root -p
```

##
```sh
Para visualizar todos os usuários bem como as suas permissões de autenticação, veja:

mysql -u root -p -e "SELECT User,Host FROM mysql.user;"

Podemos criar também usuários e alterar as suas permissões:

# mysql -h localhost -u root -p

> CREATE USER 'teste'@'localhost' IDENTIFIED BY 'teste';
> GRANT ALL ON bancodados.* TO 'teste'@'localhost';
> quit
```

##
```sh
Mas também podemos criar um usuário com permissões para um dominio:

mysql> CREATE USER 'teste2'@'seusite.dominio.com' IDENTIFIED BY 'teste2';

mysql> GRANT ALL ON bancodados.* TO 'teste2'@'seusite.dominio.com';

E veja o resultado:

> SELECT User,Host FROM mysql.user;
```



