
do $$
begin
   for grow in 1..50 loop
    insert into public.flowerapp_orders (order_time, order_product, order_quantity, order_subtotal, order_total)
	values (timestamp '2021-01-10 20:00:00' + random() * (timestamp '2000-01-20 20:00:00' - timestamp '2021-01-10 10:00:00'),
			'Product' || floor(random() * 20 + 1),
			floor(random() * 10000 + 1),
			floor(random() * 10000 + 1) + ROUND(random()::numeric,1), 
            floor(random() * 10000 + 1) + ROUND(random()::numeric,1));
   end loop;
end; $$