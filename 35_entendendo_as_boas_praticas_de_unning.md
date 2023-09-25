##
```sh
echo [PID]  [MEM]  [PATH] &&  ps aux | awk '{print $2, $4, $11}' | sort -k2rn | head -n 20

ps -eo pcpu,pid,user,args | sort -k 1 -r | head -20

curl -L http://mysqltuner.pl/ | perl

vim /etc/mysql/mysql.conf.d/mysqld.cnf
```
