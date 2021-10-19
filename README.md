# avalah_app with Postgresql + Django


### 1. Clone the project and start Docker in bg

- _git clone https://github.com/VkHyperNova/avalah_app.git_

### 2. Go to project folder and in terminal type:

- _docker-compose up --build_

### 3. When its done press (should say: database system is ready to accept connections)

- _CTRL + C_ **(to close)**

### 4. And Run:

- _docker-compose up_

### 5. In Browser Goto:

- _http://127.0.0.1:8000_ **(NB! Not '0.0.0.0:8000' like it says in console)**

### 6. About mock data:

 I created a folder named **_'sql'_**. There are 2 files: **_'create_tables.sql'_** and **_'fill_tables.sql'_**


**_NB!_** They run automatically when the project is created. It's definned in **_docker-compose.yml_** under -> **_db_** -> **_volumes_**.

### **(OPTIONAL) If you want more data you can run the _fill_tables.sql_ from commandline while project is running**

_Open new commandline in project folder:_

- _docker exec -u postgres avalah_app-db-1 psql postgres postgres -f docker-entrypoint-initdb.d/fill_tables.sql_

### 7. APIS

 **a) List of all products (in paginated manner)**

_In browser type:_

_Display all products_

- _http://127.0.0.1:8000/products_

_Custom page size (size=3)_

- _http://127.0.0.1:8000/products?size=3_

_Custom page number and size (page=2, size=3)_

- _http://127.0.0.1:8000/products?page=2&size=3_


**b) List of all orders (0)**

- _http://127.0.0.1:8000/orders_

_Custom page size (size=3)_

- _http://127.0.0.1:8000/orders?size=3_

_Custom page number and size (page=2, size=3)_

- _http://127.0.0.1:8000/orders?page=2&size=3_


**c) Finds related products given a product identifier**

_Sample Product with id 5_

- _http://127.0.0.1:8000/products/5_

_Custom page size (size=3)_

- _http://127.0.0.1:8000/products/5?size=3_
 
_Custom page number and size (page=1, size=2)_

- _http://127.0.0.1:8000/products/5?page=1&size=2_

