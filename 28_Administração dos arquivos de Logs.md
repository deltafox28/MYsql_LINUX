# Administração dos arquivos de Logs

##
```sh
vim /etc/mysql/mysql.conf.d/mysqld.cnf

[mysqld]

log_error=/var/log/mysql/mysql_error.log
general_log_file        = /var/log/mysql/mysql.log
general_log             = 1
log_slow_queries       = /var/log/mysql/mysql-slow.log
long_query_time = 2
log-queries-not-using-indexes
```

##
```sh
 systemctl restart mysql.service

 tail -100 /var/log/mysql/mysql.log

 tail -100 /var/log/mysql/mysql-slow.log

SET GLOBAL general_log = 'ON';
SET GLOBAL slow_query_log = 'ON';

SET GLOBAL general_log = 'OFF';
SET GLOBAL slow_query_log = 'OFF';

 vim /etc/logrotate.d/mysql-server

show variables like '%log%';

Links de ref:
https://dev.mysql.com/doc/refman/8.0/en/server-logs.html
```
