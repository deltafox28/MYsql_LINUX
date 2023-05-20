# Trabalhando com buscas com GROUP BY

##
```sh
SELECT COUNT(*) FROM mail;

SELECT srcuser, COUNT(*) FROM mail GROUP BY srcuser;

SELECT srcuser, COUNT(*) FROM mail GROUP BY srcuser;

SELECT srcuser, SUM(size) AS 'total de bytes', AVG(size) AS 'bytes por msg' FROM mail GROUP BY srcuser;

SELECT srcuser, srchost, COUNT(srcuser) FROM mail GROUP BY srcuser, srchost;

SELECT srcuser, MAX(size), MAX(t) FROM mail GROUP BY srcuser;

SELECT srcuser, dstuser, MAX(size) FROM mail GROUP BY srcuser, dstuser;

SELECT nome, MAX(milhas) AS 'viagem mais longa' FROM log_moto GROUP BY nome;

SELECT srcuser, dstuser, MAX(size) FROM mail GROUP BY srcuser, dstuser;

SELECT nome, MAX(milhas) AS 'viagem mais longa' FROM log_moto GROUP BY nome;
```
