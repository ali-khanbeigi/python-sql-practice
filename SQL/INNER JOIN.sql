SELECT * FROM Sales.Orders 
SELECT * FROM Sales.Customers 
SELECT * FROM HR.Employees 
SELECT O.orderid, H.firstname, H.lastname from sales.Orders	O
INNER JOIN HR.Employees H ON H.empid=O.empid
INNER JOIN sales.Customers c on c.custid=O.custid
