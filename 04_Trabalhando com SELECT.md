# Trabalhando com SELECT

##
```sh
wget https://raw.githubusercontent.com/Mazuco/MySQL/master/mail.sql

mysql teste -u root -p < mail.sql
```

##
```sh
mysql -u root  -p

USE teste;

SELECT * FROM mail;


SELECT srcuser, srchost, t, size FROM mail;
```

##
```sh
SELECT t, srcuser, srchost FROM mail WHERE srchost = 'venus';

SELECT t, srcuser, srchost FROM mail WHERE srchost LIKE 's%';

SELECT * FROM mail WHERE srcuser = 'teste1' AND dstuser = 'ronaldo';

SELECT t, CONCAT(srcuser,'@',srchost), size FROM mail;
```

##
```sh
SELECT DATE_FORMAT(t,'%e de %M de %Y'), CONCAT(srcuser,'@',srchost), size FROM mail;

SELECT DATE_FORMAT(t,'%e de %M de %Y') AS data_envio, CONCAT(srcuser,'@',srchost) AS remetente, size FROM mail;

SELECT DATE_FORMAT(t,'%M %e, %Y') AS 'Data da mensagem', CONCAT(srcuser,'@',srchost) AS 'Remetente da mensagem', size AS 'Número em bytes' FROM mail;

SELECT t, srcuser, dstuser, size/1024 AS kilobytes FROM mail WHERE size/1024 > 500;
```

##
```sh
SELECT * FROM mail WHERE dstuser = 'ronaldo' ORDER BY srchost, srcuser;

SELECT * FROM mail WHERE size > 50000 ORDER BY size DESC;

SELECT srcuser FROM mail;
```

##
```sh
SELECT COUNT(DISTINCT srcuser) FROM mail;

SELECT DISTINCT YEAR(t), MONTH(t), DAYOFMONTH(t) FROM mail;

SELECT COUNT(DISTINCT srcuser) FROM mail;

SELECT DISTINCT YEAR(t), MONTH(t), DAYOFMONTH(t) FROM mail;
```


