SELECT BillingCountry, SUM(Total) AS TotalSales
FROM invoices
GROUP BY BillingCountry;

SELECT substr(InvoiceDate, 1, 4) AS Year, SUM(Total) AS TotalSales
FROM invoices
GROUP BY Year;

SELECT BillingState, SUM(Total) AS TotalSales
FROM invoices
WHERE BillingCountry = 'USA' AND InvoiceDate > '2010-01-01'
GROUP BY BillingState;

SELECT BillingCountry, MAX(Total) AS MaxOrderAmount
FROM invoices
WHERE BillingCountry = 'Germany' OR BillingCountry = 'France'
GROUP BY BillingCountry;