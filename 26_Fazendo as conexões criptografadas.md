# Fazendo as conexões criptografadas


##
```sh
SHOW VARIABLES LIKE '%ssl%';

 mysql_ssl_rsa_setup --uid=mysql

 find /var/lib/mysql -name '*.pem' -ls

 vim /etc/mysql/mysql.conf.d/mysqld.cnf

ssl-ca=/var/lib/mysql/ca.pem
ssl-cert=/var/lib/mysql/server-cert.pem
ssl-key=/var/lib/mysql/server-key.pem
require_secure_transport = ON

systemctl restart mysql
```

##
```sh
mysql -u root -p --ssl-mode=REQUIRED

SHOW VARIABLES LIKE '%ssl%';

CREATE USER 'testessl'@'%' IDENTIFIED BY '123456' REQUIRE SSL;

CREATE DATABASE exemplo;

GRANT ALL ON exemplo.* TO 'testessl'@'%';

FLUSH PRIVILEGES;

mysql -u testessl -p -h 192.168.0.20 -P 3306 --ssl

\s

-- Liks de Ref:
-- https://dev.mysql.com/doc/refman/8.0/en/encrypted-connection-options.html
-- https://dev.mysql.com/doc/refman/8.0/en/using-encrypted-connections.html
```
