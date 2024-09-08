-- Keep a log of any SQL queries you execute as you solve the mystery.

-- know the day and where crime took place to find id and crime description
SELECT * FROM crime_scene_reports
WHERE day = 28 AND month = 7
AND street = 'Humphrey Street';

-- get info from interviews on teh same day
SELECT * FROM interviews
WHERE day = 28 AND month = 7;

-- within ten minutes called someone to purchase earliest flight out of fiftyville tomorrow for them
-- withdrew money from atm before crime on Leggett St

-- names of people who withdrew from specified atm on crime day
SELECT DISTINCT name FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE atm_transactions.account_number IN
(SELECT account_number FROM atm_transactions
WHERE day = 28 AND month = 7
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw');



--callers + atm withdraw aka perpetrators
SELECT name FROM people
WHERE phone_number IN
(SELECT caller FROM phone_calls
WHERE day = 28 AND month = 7
AND duration < 60
AND caller IN
(SELECT phone_number FROM people
WHERE name IN
(SELECT DISTINCT name FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE atm_transactions.account_number IN
(SELECT account_number FROM atm_transactions
WHERE day = 28 AND month = 7
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw'))));

--recievers + atm withdraw aka accomplices
SELECT name FROM people
WHERE phone_number IN
(SELECT receiver FROM phone_calls
WHERE day = 28 AND month = 7
AND duration < 60
AND caller IN
(SELECT phone_number FROM people
WHERE name IN
(SELECT DISTINCT name FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE atm_transactions.account_number IN
(SELECT account_number FROM atm_transactions
WHERE day = 28 AND month = 7
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw'))));


--people on the earliest flight aka perpetrators
SELECT name FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
WHERE passengers.flight_id IN
(SELECT id FROM flights
WHERE day = 29 AND month = 7
ORDER BY hour, minute
LIMIT 1);



--people who left bakery after 10:15 aka perpatraitor
SELECT name FROM people
WHERE license_plate IN
(SELECT license_plate FROM bakery_security_logs
WHERE day = 28 AND month = 7
AND hour = 10 and minute > 15
AND activity = 'exit');

-- thief is bruce
--where is bruce going
SELECT city FROM airports WHERE id = (SELECT destination_airport_id FROM flights
WHERE id = (SELECT flight_id FROM passengers WHERE passport_number = (SELECT passport_number from people WHERE name = 'Bruce')));