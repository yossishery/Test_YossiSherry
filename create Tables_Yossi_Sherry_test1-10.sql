#DECLARE @num1 int;
SET @num1 = 0;

#DECLARE @num2 int ;
SET @num2= 0;

#DECLARE @MyTableName nvarchar (200);
SET @MyTableName='';

#DECLARE @SourceTableName nvarchar (200); 
SET @SourceTableName = 'YossiSherry_AllUsers';

#DECLARE  @DynamicSQL nvarchar  (1000);
SET @DynamicSQL='';

WHILE  @num1 != 100  DO

SET @MyTableName ='Yossi_Sherry_TEST_'
SET @num1 = @num1+10
SET @num2 = @num1+9

SET @MyTableName = @MyTableName+'_'+ CONVERT(varchar,@num1)
SET @DynamicSQL = N'SELECT * INTO ' + @MyTableName + ' FROM ' + @SourceTableName +' WHERE dob_age between '+ convert(varchar,@num1) + ' and '+ convert(varchar,@num2)

#select @DynamicSQL,@MyTableName

EXECUTE (@DYNAMICSQL) 
  
END WHILE;








