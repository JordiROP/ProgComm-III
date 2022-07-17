INSERT INTO "employee" ("first_name", "last_name") VALUES ('Victor', 'Altés Gaspar');
INSERT INTO "employee" ("first_name", "last_name") VALUES ('Salma', 'Assiad Sebai');

INSERT INTO "customer" ("customer_name", "city_id", "customer_address", "next_call_date", "ts_inserted") VALUES ('Abraham Castro Criado', 1, 'Calle de la Piruleta', '2022-12-01','2022-12-01');
INSERT INTO "customer" ("customer_name", "city_id", "customer_address", "next_call_date", "ts_inserted") VALUES ('Pelayo Cobos Rodriguez', 1, 'Salchichon', '2022-05-01', '2022-05-01');
INSERT INTO "customer" ("customer_name", "city_id", "customer_address", "next_call_date", "ts_inserted") VALUES ('Artur Cullerés Cervera', 2, 'Sanjacobo Street', '2022-01-01', '2022-01-01');
INSERT INTO "customer" ("customer_name", "city_id", "customer_address", "next_call_date", "ts_inserted") VALUES ('Didac Colominas Abalde', 3, 'Albacete Strassen', '2022-08-01', '2022-08-01');
INSERT INTO "customer" ("customer_name", "city_id", "customer_address", "next_call_date", "ts_inserted") VALUES ('Eduard de La Arada Janoher', 1, 'Wala wala bing bong', '2022-07-01', '2022-07-01');

INSERT INTO "call" ("employee_id", "customer_id", "start_time", "end_time", "call_outcome_id") VALUES (1, 1, '2022-12-01 12:05:06', '2022-12-01 12:06:06', 0);
INSERT INTO "call" ("employee_id", "customer_id", "start_time", "end_time", "call_outcome_id") VALUES (1, 2, '2022-05-01 17:11:06', '2022-05-01 17:24:06', 0);
INSERT INTO "call" ("employee_id", "customer_id", "start_time", "end_time", "call_outcome_id") VALUES (2, 3, '2022-01-01 22:01:06', '2022-01-01 22:01:45', 0);
INSERT INTO "call" ("employee_id", "customer_id", "start_time", "end_time", "call_outcome_id") VALUES (2, 4, '2022-08-01 11:43:06', '2022-08-01 11:55:06', 0);
INSERT INTO "call" ("employee_id", "customer_id", "start_time", "end_time", "call_outcome_id") VALUES (1, 5, '2022-07-01 04:22:06', '2022-07-01 05:22:06', 0);

INSERT INTO "city" ("name") VALUES ('Lleida');
INSERT INTO "city" ("name") VALUES ('Murcia');
INSERT INTO "city" ("name") VALUES ('Barcelona');