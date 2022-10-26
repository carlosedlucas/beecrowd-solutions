SELECT a.name, b.name
FROM products as a
JOIN providers as b
ON a.id_providers = b.id
JOIN categories as c
ON c.id = a.id_categories
WHERE c.id = 6
