delimiter \\
drop table if exists singleupdate;\\
delimiter \\
drop table if exists singleupdate2;\\
create procedure singleupdate2 (
in tablename  varchar(50), 
in columnname varchar(50),
in valuechange varchar(50),
in idname varchar(50),
in idparam int
)
begin
set @statement= concat('update ' ,tablename,' set ',columnname,' =\'',valuechange ,'\'',' where ',idname,'=',idparam);
prepare stm from  @statement;
execute stm;
end\\
delimiter ;
call singleupdate2('srii_user_lists','name','srinidhi','sno',1);
select *from srii_user_lists;

