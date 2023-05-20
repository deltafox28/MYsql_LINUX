# Trabalhando com o comando LIMIT

##
```sh
wget https://raw.githubusercontent.com/Mazuco/MySQL/master/perfil.sql

mysql teste -u root -p < perfil.sql

mysql -u root -p
```

##
```sh
USE teste;

SELECT * FROM perfil;

SELECT * FROM perfil LIMIT 1;

SELECT * FROM perfil LIMIT 4;

SELECT * FROM perfil ORDER BY nascimento LIMIT 1;

SELECT * FROM perfil ORDER BY nascimento DESC LIMIT 1;

SELECT nome, DATE_FORMAT(nascimento,'%d-%m') AS Nascido FROM perfil ORDER BY Nascido LIMIT 1;

SELECT nome, DATE_FORMAT(nascimento,'%d-%m') AS Nascido FROM perfil ORDER BY Nascido LIMIT 3;

SELECT COUNT(*) FROM perfil;
```
