# Instalação do MySQL em Ubuntu CentOS

##
```sh
https://downloads.mysql.com/archives/community/ (A central de Donwlods do MySQL)
```

##
```sh
Ubuntu:
wget -c https://dev.mysql.com/get/mysql-apt-config_0.8.10-1_all.deb 

sudo dpkg -i mysql-apt-config_0.8.10-1_all.deb 

sudo apt update

sudo apt-get install mysql-server

systemctl status mysql

systemctl enable mysql

mysql -u root -p
```

##
```sh
CentOS:
yum localinstall https://dev.mysql.com/get/mysql80-community-release-el7-1.noarch.rpm

yum install mysql-community-server

systemctl start mysqld.service 

systemctl enable mysqld.service

Agora para acessar:

grep 'temporary password' /var/log/mysqld.log

mysql -u root -p

mysql -h localhost -u root -p

ALTER USER 'root'@'localhost' IDENTIFIED BY 'MinhaSenha6!';

Para habilitar o acesso remoto do CentOS, use:

firewall-cmd --permanent --zone=public --add-service=mysql 
firewall-cmd --permanent --zone=public --add-port=3306/tcp

systemctl restart firewalld.service
E pode testar via remoto
mysql -h 10.0.15.25 -u root -p
```










