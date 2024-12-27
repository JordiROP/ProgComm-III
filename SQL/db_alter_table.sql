ALTER TABLE "customer"
ADD CONSTRAINT "FK_CityCustomer"
FOREIGN KEY ("city_id") REFERENCES "city"("id");

ALTER TABLE "city"
ADD COLUMN "country_code" VARCHAR(5) DEFAULT 'ES';