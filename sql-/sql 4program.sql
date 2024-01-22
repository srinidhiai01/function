use ai_srinidhi_detailsdb;
create table srii_user_lists(sno int not null primary key auto_increment,
name varchar(50),
email varchar(50),
gender varchar(50),
qualification varchar(50)
);
delimiter \\
create procedure srii_user_lists( in snoparameter int,
in nameparameter varchar(50),
in emailparameter varchar(50),
genderparameter varchar(50),
in qualificationparameter varchar(50)
)
begin
insert into srii_user_lists(sno,name,email,gender,qualification) values (sno,nameparameter,emailparameter,genderparameter,qualificationparameter);
end \\
delimiter ;
select*from srii_user_lists;
call srii_user_lists(1,'sri','sri@gmail.com','female','bsc');
call srii_user_lists(2,'tamil','tamil@gmail.com','female','bsc');
call srii_user_lists(3,'snega','snega@gmail.com','female','bsc');
call srii_user_lists(4,'punitha','punitha@gmail.com','female','bcom');


