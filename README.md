# avalah_app with Postgresql + Django


1) Clone the project and start Docker in bg

-> git clone https://github.com/VkHyperNova/avalah_app.git

2) Go to project folder and open terminal

Run:
-> docker-compose up --build

When its done press
-> CTRL + C (to close)

And Run:
-> docker-compose up

In Browser Goto:
-> 127.0.0.1:8000 (it should say: avalah app)

3) About mock data:

- I created a folder named 'sql'
- There are 2 files: 'create_tables.sql' and 'fill_tables.sql'

NB! They run automatically when the project is created. The commands are in docker-compose.yml under -> db -> volumes.

- You can run the fill_tables.sql from commandline while project is running (if you want more data)

(Open new commandline in project folder)

-> docker exec -u postgres avalah_app-db-1 psql postgres postgres -f docker-entrypoint-initdb.d/fill_tables.sql

4) APIS

- List of all products (in paginated manner)


In browser type:

(To return product list with default page number(1) and size(5))

-> http://127.0.0.1:8000/products

(For custom page number and size edit numbers in '?page=2&size=3' part of url)

-> http://127.0.0.1:8000/products?page=2&size=3


- List of all orders (0)

-> http://127.0.0.1:8000/orders

-> http://127.0.0.1:8000/orders?page=2&size=3


- Finds related products given a product identifier

-> http://127.0.0.1:8000/products/5

