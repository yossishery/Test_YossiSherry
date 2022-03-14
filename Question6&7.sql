/*Q_6*/

select  *
from
		(
		select distinct * from YossiSherry_Test_20 
		union 
		select distinct * from YossiSherry_Test_5 
		) as d
order by name_first ;


/*Q_7*/

select *
from

(
select * from YossiSherry_Test_20 
union all
select * from YossiSherry_Test_5 
) as d
order by name_first ;



