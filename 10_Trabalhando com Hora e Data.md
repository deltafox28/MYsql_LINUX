# Trabalhando com Hora e Data

##
```sh
DROP TABLE IF EXISTS tempo_val;
CREATE TABLE tempo_val
(
  t1  TIME,
  t2  TIME
);

INSERT INTO tempo_val (t1,t2) VALUES('12:00:00','15:00:00');
INSERT INTO tempo_val (t1,t2) VALUES('05:01:30','02:30:20');
INSERT INTO tempo_val (t1,t2) VALUES('12:30:20','18:30:45');

SELECT * FROM tempo_val;

DROP TABLE IF EXISTS data_val;
CREATE TABLE data_val
(
  d DATE
);

INSERT INTO data_val (d) VALUES('1864-02-28');
INSERT INTO data_val (d) VALUES('1900-01-15');
INSERT INTO data_val (d) VALUES('1999-12-31');
INSERT INTO data_val (d) VALUES('2000-06-04');
INSERT INTO data_val (d) VALUES('2017-03-16');
```

##
```sh
SELECT t1, t2 FROM tempo_val;

SELECT d FROM data_val;

SELECT CURDATE(), CURTIME(), NOW();

SELECT CURTIME(), CURTIME(2), CURTIME(6);


SELECT d, DATE_FORMAT(d,'%d de %M de %Y') FROM data_val;

SELECT d AS 'Data', DATE_FORMAT(d,'%M %d, %Y') AS 'Formato de hora' FROM data_val;
```

##
```sh
DROP TABLE IF EXISTS hora_tempo;
CREATE TABLE hora_tempo
(
  dt  DATETIME
);

INSERT INTO hora_tempo (dt) VALUES('1970-01-01 00:00:00');
INSERT INTO hora_tempo (dt) VALUES('1999-12-31 09:00:00');
INSERT INTO hora_tempo (dt) VALUES('2000-06-04 15:45:30');
INSERT INTO hora_tempo (dt) VALUES('2017-03-16 12:30:15');
```

##
```sh
SELECT * FROM hora_tempo;

SELECT dt, DATE_FORMAT(dt,'%e/%c/%y %r') AS 'formato 1', DATE_FORMAT(dt,'%e de %M de %Y as %T') AS 'formato 2' FROM hora_tempo;

SELECT CURDATE(), DATE_ADD(CURDATE(),INTERVAL 3 DAY);

SELECT CURDATE(), DATE_SUB(CURDATE(),INTERVAL 1 WEEK);

SELECT NOW(), DATE_ADD(NOW(),INTERVAL 84 HOUR);

SELECT NOW(), DATE_ADD(NOW(),INTERVAL '87:24' HOUR_MINUTE);
```

