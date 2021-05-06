
# Postgresql errors when testing - some notes :

## error 1
    could not connect to server: Connection refused(0x0000274D/10061)
    Is the server running on host "192.168.1.9" and accepting
    TCP/IP connections on port 5432?

##### CHANGE THE LISTEN ADDRESS
By default, PostgreSQL DB server listen address is set to the 'localhost' , and we need to change it so it accepts connection from any IP address; or you can use comma separated list of addresses. 
#### edit postgresql.conf
    pi@pi4:/# grep listen /etc/postgresql/11/main/postgresql.conf  
    listen_addresses = 'localhost'	
#	
    change 'localhost' to '*'
#
## error 2
    FATAL:  no pg_hba.conf entry for host "192.168.1.10", user "user3", database "suppliers", SSL on        
    FATAL:  no pg_hba.conf entry for host "192.168.1.10", user "user3", database "suppliers", SSL off

##### OPEN POSTGRESQL TO THE WORLD    
#### edit pg_hba.conf

    pi@pi4:/# vim /etc/postgresql/11/main/pg_hba.conf

    add at end, new line 
#
    host all all 0.0.0.0/0 md5
#

## restart postgresql
    /etc/init.d/postgresql restart
#
## error 3
    FATAL:  database "suppliers" does not exist
    Make sure your database name matches your python code and ini file!


https://bosnadev.com/2015/12/15/allow-remote-connections-postgresql-database-server/