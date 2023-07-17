## fix mariadb index length bug
How to solve the “Specified key was too long; max key length is 767 bytes” error in MariaDB
This error occurs when you try to create a unique index on a column or a combination of columns that exceeds the maximum key length of 767 bytes for InnoDB tables or 1000 bytes for MyISAM tables. This limit depends on the character set and collation of the columns, as well as the global settings of MariaDB.

One possible solution is to change some global settings of MariaDB to allow longer indexes. This requires modifying the my.ini file or using SET GLOBAL commands. For example:

SET GLOBAL innodb_file_format = Barracuda;
SET GLOBAL innodb_file_per_table = on;
SET GLOBAL innodb_default_row_format = dynamic;
SET GLOBAL innodb_large_prefix = 1;
SET GLOBAL innodb_file_format_max = Barracuda;
Copy
This will enable the Barracuda file format, which supports longer indexes for dynamic or compressed row formats. You also need to set innodb_large_prefix to 1 to allow index key prefixes longer than 767 bytes. Note that these settings may not be compatible with older versions of MariaDB or MySQL.

After changing these settings, you need to restart the MariaDB server and then run your migrations again.