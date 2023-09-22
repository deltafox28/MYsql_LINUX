# phpMyAdmin

##
```sh
apt-get update
apt-get install phpmyadmin php-mbstring php-gettext

phpenmod mbstring

systemctl restart apache2
```

##
```sh
SELECT user,authentication_string,plugin,host FROM mysql.user;

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456';

FLUSH PRIVILEGES;

SELECT user,authentication_string,plugin,host FROM mysql.user;

http://seuip/phpmyadmin/
```

##
```sh
vim /etc/apache2/conf-available/phpmyadmin.conf

<Directory /usr/share/phpmyadmin>
    Options FollowSymLinks
    DirectoryIndex index.php
    AllowOverride All

systemctl restart apache2

vim /usr/share/phpmyadmin/.htaccess

AuthType Basic
AuthName "Restricted Files"
AuthUserFile /etc/phpmyadmin/.htpasswd
Require valid-user

htpasswd -c /etc/phpmyadmin/.htpasswd teste

http://192.168.0.20/phpmyadmin/

Links de ref:
https://www.phpmyadmin.net/
```
