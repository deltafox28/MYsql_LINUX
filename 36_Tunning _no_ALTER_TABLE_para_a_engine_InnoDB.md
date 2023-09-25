##
```sh
# git clone https://github.com/datacharmer/test_db.git

# cd test_db/

# mysql -t -u root -p < employees.sql

USE employees

ALTER TABLE salaries 
ADD COLUMN remark VARCHAR(32) DEFAULT NULL
AFTER to_date,
ADD INDEX IDX_FROMDATE(from_date);


-- Em outra conexão com root, execute esse comando para a análise de tempo:

SHOW FULL PROCESSLIST \G

-- Links de ref
-- https://dev.mysql.com/doc/employee/en/employees-installation.html

```
