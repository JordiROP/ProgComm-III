CREATE TABLE "city" (
    "id" serial primary key not null,
    "name" varchar(255) not null
);

ALTER TABLE "customer"
ADD CONSTRAINT "FK_CityCustomer"
FOREIGN KEY ("city_id") REFERENCES "city"("id");