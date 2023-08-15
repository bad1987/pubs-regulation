# FastAPI App Setup

## Virtual Environment Activation
1. Activate your virtual environment.

## Environment Variables
1. Create a `.env` file in the root directory of your project.
2. Set the following options in the `.env` file:
   - MARIADB_HOST: `<your_MariaDB_host>`
   - MARIADB_PORT: `<your_MariaDB_port>`
   - MARIADB_USER: `<your_MariaDB_username>`
   - MARIADB_PASSWORD: `<your_MariaDB_password>`
   - MARIADB_DB: `<your_MariaDB_database>`
   - ALLOWED_ORIGINS: `<allowed_origins>`
   - ADMIN_USERNAME: `<admin_username>`
   - ADMIN_EMAIL: `<admin_email>`
   - ADMIN_PASSWORD: `<admin_password>`
   - COOKIE_SECURE: `<cookie_secure_option>`

## Requirements Installation
1. Install the required dependencies by running the following command:
   ```shell
   pip install -r requirements.txt
   ```
## Database Migrations
1. Move to the migrations directory.
2. Run the following command to generate and apply the migrations:
   ```shell
   alembic revision --autogenerate
   alembic upgrade head
   ```
## Seed Admin User
1. Move to the seeders directory.
2. Run the admin_seed.py script to seed the admin user:
   ```shell
   python admin_seed.py
   ```

## Running the Development Server
1. Run the following command to start the development server in the root directory of your project:
   ```shell
   uvicorn main:app --reload
   ```

Now your FastAPI app should be running. Access it through the specified server URL.

```
Please note that this Markdown document assumes basic familiarity with command-line interface (CLI) usage. Make sure to modify the instructions as needed to match your specific project structure and environment setup.
```

## fix mariadb index length bug
How to solve the “Specified key was too long; max key length is 767 bytes” error in MariaDB
This error occurs when you try to create a unique index on a column or a combination of columns that exceeds the maximum key length of 767 bytes for InnoDB tables or 1000 bytes for MyISAM tables. This limit depends on the character set and collation of the columns, as well as the global settings of MariaDB.

One possible solution is to change some global settings of MariaDB to allow longer indexes. This requires modifying the my.ini file or using SET GLOBAL commands. For example:

SET GLOBAL innodb_file_format = Barracuda;
SET GLOBAL innodb_file_per_table = on;
SET GLOBAL innodb_default_row_format = dynamic;
SET GLOBAL innodb_large_prefix = 1;
SET GLOBAL innodb_file_format_max = Barracuda;
This will enable the Barracuda file format, which supports longer indexes for dynamic or compressed row formats. You also need to set innodb_large_prefix to 1 to allow index key prefixes longer than 767 bytes. Note that these settings may not be compatible with older versions of MariaDB or MySQL.

After changing these settings, you need to restart the MariaDB server and then run your migrations again.