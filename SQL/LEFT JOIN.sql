select * from Sales.Customers
select * from hr.Employees
insert into HR.Employees(lastname,firstname,title,titleofcourtesy,birthdate,hiredate,address,city,region,postalcode,country,phone,mgrid)
values('test','test1','MR','TEST',GETDATE(),GETDATE(),'TEST','TEST','TEST','TEST','C','C',null)

SELECT O.orderid,H.firstname,H.lastname FROM  HR.Employees H
LEFT JOIN Sales.Orders O ON H.empid=O.empid 

select productid, sum(qty) sumqty from sales.OrderDetails
where productid>25
group by productid
having sum(qty)>1000
order by sumqty desc
 
