SELECT *
FROM "call"
WHERE employee_id=1
ORDER BY id;

SELECT *
FROM "call"
INNER JOIN "customer"
ON "call".customer_id = "customer".id
WHERE "call".customer_id = 1;