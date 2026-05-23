
CREATE VIEW SALESVIEW AS
SELECT O.orderid,O.orderdate , OD.productid , OD.qty, OD.unitprice FROM Sales.Orders O
INNER JOIN Sales.OrderDetails OD ON O.orderid=OD.orderid
 
SELECT * FROM SALESVIEW

