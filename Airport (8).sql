
---1
ALTER TABLE Passengers
ADD CONSTRAINT check_age_10_years CHECK (
    EXTRACT(YEAR FROM AGE(date_of_birth)) >= 10
);

--2
ALTER TABLE Booking
ADD CONSTRAINT check_price_range CHECK (
    ticket_price BETWEEN 0 AND 50000
);

--3
ALTER TABLE Baggage
ADD CONSTRAINT check_weight_range CHECK (
    weight_in_kg BETWEEN 1 AND 23
);

--4
ALTER TABLE Airport
ADD CONSTRAINT check_airport_name_length CHECK (
    LENGTH(airport_name) >= 10
);


--6
ALTER TABLE Passengers
ADD CONSTRAINT check_gender_age CHECK (
    (gender = 'Male' AND EXTRACT(YEAR FROM AGE(date_of_birth)) >= 18) OR
    (gender = 'Female' AND EXTRACT(YEAR FROM AGE(date_of_birth)) >= 19)
);

--7
ALTER TABLE Passengers
ADD CONSTRAINT check_country_age CHECK (
    (country_of_citizenship = 'Kazakhstan' AND EXTRACT(YEAR FROM AGE(date_of_birth)) >= 18) OR
    (country_of_citizenship = 'France' AND EXTRACT(YEAR FROM AGE(date_of_birth)) >= 17) OR
    (country_of_citizenship NOT IN ('Kazakhstan', 'France') AND EXTRACT(YEAR FROM AGE(date_of_birth)) >= 19)
);


--8
--ALTER TABLE Booking
--ADD COLUMN ticket_discount DECIMAL(5, 2);

ALTER TABLE Booking
ADD CONSTRAINT check_ticket_discount CHECK (
    (created_at >= '2024-01-01' AND ticket_discount = 0.05) OR
    (created_at < '2024-01-01' AND ticket_discount = 0.10)
);