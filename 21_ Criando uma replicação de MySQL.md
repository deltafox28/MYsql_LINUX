# Criando uma replicação de MySQL


## MASTER
```sh
vim /etc/mysql/mysql.conf.d/mysqld.cnf

server_id           = 1
log_bin             = /var/log/mysql/mysql-bin.log
log_bin_index       = /var/log/mysql/mysql-bin.log.index
relay_log           = /var/log/mysql/mysql-relay-bin
relay_log_index     = /var/log/mysql/mysql-relay-bin.index
expire_logs_days    = 10
max_binlog_size     = 100M
log_slave_updates   = 1
auto-increment-increment = 2
auto-increment-offset = 1

bind-address    = 0.0.0.0

# SLAVE

server_id           = 2
log_bin             = /var/log/mysql/mysql-bin.log
log_bin_index       = /var/log/mysql/mysql-bin.log.index
relay_log           = /var/log/mysql/mysql-relay-bin
relay_log_index     = /var/log/mysql/mysql-relay-bin.index
expire_logs_days    = 10
max_binlog_size     = 100M
log_slave_updates   = 1
auto-increment-increment = 2
auto-increment-offset = 2

bind-address    = 0.0.0.0
```

## 
```sh
Depois, dê um restart em ambos os banco de dados:

sudo service mysql restart

 Agora, vamos criar um usuário para a replicação:

mysql -u root -p


CREATE USER 'replication'@'%' IDENTIFIED BY '123456';

GRANT REPLICATION SLAVE ON *.* TO 'replication'@'%';

FLUSH PRIVILEGES;
```


##
```sh
 Vá na máquina Slave para ver se esta conectando:

mysql -u replication -p -h 192.168.0.19 -P 3306

 Depois volte para a máquina Master:

SHOW MASTER STATUS;

 Agora no Slave rode esses comandos, e coloque as informações da Master conforme demostrado anteriormente:

STOP SLAVE;

CHANGE MASTER TO master_host='192.168.0.19', master_port=3306, master_user='replication', master_password='123456', master_log_file='mysql-bin.000006', master_log_pos=873;


START SLAVE;


SHOW SLAVE STATUS\G
```


##
```sh 
 Veja se as seguintes variaveis estão assim:

Slave_IO_State: Waiting for master to send event
Slave_IO_Running: Yes
Slave_SQL_Running: Yes

 Agora, vamos na máquina Master e criar um banco de dados e uma tabela com conteúdo nela:

create database teste_ha;
create table teste_ha.flores (`id` varchar(10));

SLAVE

show tables in teste_ha;

 Pronto!


Links de ref:

https://dev.mysql.com/doc/refman/8.0/en/replication.html
```



