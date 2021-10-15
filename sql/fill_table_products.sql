
do $$
begin
   for grow in 1..20 loop
    insert into public.flowerapp_products (product_name, product_stock, product_price, product_popularity)
	values ('Product' || grow, floor(random() * 10000 + 1),floor(random() * 10 + 1) + ROUND(random()::numeric,1), floor(random() * 1000 + 1));
   end loop;
end; $$








