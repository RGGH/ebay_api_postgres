# Install postgresql (Linux example)
    sudo apt-get install postgresql
## switch to postgres user
    sudo -i -u postgres
## start postgresql
    psql
## create new database
    CREATE DATABASE ebay;
## connect to the new database
    postgres=# \c ebay
    You are now connected to database "ebay" as user "postgres".
## create table 1
    ebay=#CREATE TABLE api_data(
    id serial, description varchar(100),price money, postage money, time_left time);
## create table 2
    ebay=#CREATE TABLE sold_data
    (id serial, description varchar(100), price money, postage money, sold_date time);
## check table 2
    ebay=# \dt sold_data

    ebay=# \dt sold_data
            List of relations
    Schema |   Name    | Type  |  Owner
    --------+-----------+-------+----------
    public | sold_data | table | postgres
    (1 row)
## check table 1
    ebay=# \dt api_data

    ebay=# \dt api_data
            List of relations
    Schema |   Name   | Type  |  Owner
    --------+----------+-------+----------
    public | api_data | table | postgres
    (1 row)