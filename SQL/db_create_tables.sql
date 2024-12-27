CREATE TABLE "employee" (
    "id" serial primary key not null,
    "first_name" varchar(255) not null,
    "last_name" varchar(255) not null
);

CREATE TABLE "customer" (
    "id" serial primary key not null,
    "customer_name" varchar(255) not null,
    "city_id" int not null,
    "customer_address" varchar(255) not null,
    "next_call_date" date,
    "ts_inserted" date
);

CREATE TABLE "call" (
    "id" serial primary key not null,
    "employee_id" int REFERENCES "employee"("id"),
    "customer_id" int REFERENCES "customer"("id"),
    "start_time" date,
    "end_time" date,
    "call_outcome_id" int
);

CREATE TABLE "city" (
    "id" serial primary key not null,
    "name" varchar(255) not null
);