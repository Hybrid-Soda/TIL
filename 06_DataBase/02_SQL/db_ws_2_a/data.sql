SELECT *
FROM artists;

SELECT COUNT(*)
FROM artists;

SELECT *
FROM artists
WHERE Name = 'AC/DC';

SELECT Name
FROM artists;

SELECT *
FROM artists
WHERE Name = 'Gilberto Gil' OR Name = 'Ed Motta';

SELECT *
FROM artists
ORDER BY Name DESC;

SELECT *
FROM artists
WHERE Name LIKE 'Vinícius%'
LIMIT 2;

SELECT ArtistId
FROM artists
ORDER BY ArtistId
LIMIT 49, 21;