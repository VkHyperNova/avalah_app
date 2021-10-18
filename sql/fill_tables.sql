
do $$
begin
   for grow in 1..20 loop
    insert into public.flowerapi_products (product_name, product_stock, product_price, product_popularity, product_category)
	values ('Flower' || grow, /* product_name */
    floor(random() * 10000 + 1), /* product_stock */
    floor(random() * 10 + 1) + ROUND(random()::numeric,1), /* product_price */
    floor(random() * 1000 + 1), /* product_popularity */
    'Category' || floor(random() * 5 + 1)); /* product_category */
   end loop;
   
   for grow in 1..50 loop
    insert into public.flowerapi_orders (order_time, order_product, order_quantity, order_subtotal, order_total)
	values (timestamp '2021-01-10 20:00:00' + random() * (timestamp '2000-01-20 20:00:00' - timestamp '2021-01-10 10:00:00'), /* order_time */
			'Flower' || floor(random() * 20 + 1), /* order_product */
			floor(random() * 100 + 1), /* order_quantity */
			floor(random() * 100 + 200) + ROUND(random()::numeric,1), /* order_subtotal */
            floor(random() * 200 + 300) + ROUND(random()::numeric,1)); /* order_total */
   end loop;
end; $$