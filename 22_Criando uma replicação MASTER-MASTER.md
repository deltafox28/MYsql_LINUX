# Criando uma replicação MASTER-MASTER

##
```sh
 MASTER 1

vim /etc/mysql/mysql.conf.d/mysqld.cnf

server-id               = 1
log_bin                 = /var/log/mysql/mysql-bin.log
expire_logs_days        = 10
max_binlog_size   = 100M

bind-address    = 0.0.0.0
```

##
```sh
 MASTER 2

vim /etc/mysql/mysql.conf.d/mysqld.cnf

server-id               = 2
log_bin                 = /var/log/mysql/mysql-bin.log
expire_logs_days        = 10
max_binlog_size         = 100M

bind-address    = 0.0.0.0
```

##
```sh
 Depois, dê um restart em ambos os banco de dados:

sudo service mysql restart

 MASTER 1

 Agora, vamos criar um usuário para a replicação:

mysql -u root -p

CREATE USER 'replication'@'%' IDENTIFIED BY '123456';

GRANT REPLICATION SLAVE ON *.* TO 'replication'@'%';

FLUSH PRIVILEGES;
```


##
```sh
 MASTER2

 Vá na máquina MASTER2 para ver se esta conectando:

mysql -u replication -p -h 192.168.0.20 -P 3306

 Depois volte para a máquina MASTER1:

SHOW MASTER STATUS;

 Agora no MASTER2 rode esses comandos, e coloque as informações da MASTER1 conforme demostrado anteriormente:

STOP SLAVE;

CHANGE MASTER TO master_host='192.168.0.20', master_port=3306, master_user='replication', master_password='123456', master_log_file='mysql-bin.000006', master_log_pos=873;


START SLAVE;


SHOW SLAVE STATUS\G
```


##
```sh 
 Veja se as seguintes variaveis estão assim:

Slave_IO_State: Waiting for master to send event
Slave_IO_Running: Yes
Slave_SQL_Running: Yes

 Agora, vamos preparar o usuário para a replicação:

CREATE USER 'replication'@'%' IDENTIFIED BY '123456';

GRANT REPLICATION SLAVE ON *.* TO 'replication'@'%';

FLUSH PRIVILEGES;
```

##
```sh
 Agora, vamos testar a conexão da MASTER 1 com a MASTER 2

mysql -u replication -p -h 192.168.0.21 -P 3306

 Agora, vamos pegar as informações da MASTER2 e depois configurar na MASTER1

SHOW MASTER STATUS;

 No MASTER1

STOP SLAVE;

CHANGE MASTER TO master_host='192.168.0.21', master_port=3306, master_user='replication', master_password='123456', master_log_file='mysql-bin.000006', master_log_pos=873;

START SLAVE;

SHOW SLAVE STATUS\G
```

##
```sh
 Agora, vamos na máquina MASTER1 e criar um banco de dados e uma tabela com conteúdo nela:

create database teste_ha;
create table teste_ha.flores (`id` varchar(10));

 MASTER2

show tables in teste_ha;

 Vamos remover o Master1

drop database teste_ha;

 MASTER2

show tables in teste_ha;

 Pronto!
```
