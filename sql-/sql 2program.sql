show databases;
create database ai_srinidhi_detailsdb;
use ai_srinidhi_detailsdb;

create table srinidhi_details(
SNO int not null primary key,
first_Name varchar(60) not null, 
middle_Name varchar(60) not null,
last_Name varchar(60) not null,
DOB date not null,
Aadhar_Number long ,
Biometric_ID long ,
Primary_Contact_No long ,
Secondary_Contact_No long ,
WhatsApp_No long ,
User_name varchar(60) not null,
Password varchar(30) not null,
UG varchar(30),
Subject_Group varchar(30),
PG varchar(30),
Subject_data varchar(30),
Year_of_Passing int,
AI_Batch_Email varchar(60),
Email varchar(60),
Address varchar(255),
District varchar(40),
Father_Name varchar(60),
 Mother_Name varchar(60));
 show tables;
 select*from srinidhi_details;
 
insert into srinidhi_details values(1,'Abdul Rahman' ,'Nil', 'B','2001-01-15',669092087983,92087983,9952630126,6369696359,9952630126,'TI2023M-C01E438','Password@123','BSC','Computer science','NIL','NIL',2022,'abdulrahmanai01@gmail.com','abdulrahman001007@gmail.com','No 3/1-76 Indra street, Keela ambikaburam Trichy-04','Trichy','Badhusha','Noorjahan');
insert into srinidhi_details values(2,'Arun','Nil','T','2002-07-07',341246643302,46643302,8525880306,6382506148,8525880306,'PU2023M-C01E488','Password@123','BSC','Computer science','NIL','NIL',2023,'arunaathi41@gmail.com', 'arunai01@gmail.com','3/4 Thirupur Thirupur(po)Kulathur(tk)Senaiyakuti Pudukkottai (Dt)-622502','Nil','Tamil selvam','Suppu laxmi');
insert into srinidhi_details values (3,'Aysha sithika','Nil', 'L','1988-01-11',784654756225,54756225,8124823036,8610353074,8124823036,'TI2023F-C01E78D','Password@123','12','Computer science','NIL','NIL','2005','ayshasithikaai01@gmail.com','aslamshabeen@gmail.com','LIGII,2801, BISMILLAH MANZIL,Anna nagar,phase 2 Navalpattu, Trichy -26','Trichy','Nazrul Islam(Husband)','Amthul jabeen');
insert into srinidhi_details values(4,'Bhavani','Nil','R','2002-10-13',935775705642,75705642,6380185097,9659871377,6380185097,'Pu2023F-C01E44D','Password@123','BSC','Computer science','NIL','NIL',2023,'bhavaniai01@gmail.com','bb464490@gmail.com','Melakkottai Kovilur (p), Alangudi Tk Pudukkottai (dt).','Pudukkottai','C.Ramachandran','R.Thenmozhi');
insert into srinidhi_details values(5,'Fathima','Nil',' M','2002-12-17',622631324614,31324614,6374041818,9791676433,6374041818,'TI2023F-C01E43B','Password@123','B.Com','Commerce','NIL','NIL','2024','Ray0488faths@gmail.com','fathimaai01@gmail.com','5/249, 20th cross, vasancity, vayalur road, trichy-620102','Trichy','Mohamed Ibrahim','Saira banu');
insert into srinidhi_details values(6,'Ghouse bi','Nil','S','1989-08-14',818393990050,93990050,9994286043,7708475065,9994286043,'TI2023F-C01E46D','Password@123','B.A.','English','NIL','NIL','2010','happydhillu@gmail.com','ghousebiai01@gmail.com','MIG 49, Phase 1, Anna nagar,TNUDP, trichy-620026.','Trichy','Juber khan. B(Husband)','Zarina Begum');
insert into srinidhi_details values(7,'Gnanagowsalya','Nil',' K','2003-04-29',418718821662,18821662,7094373123,9965452410,7094373123,'TI2023F-C01E474','Password@123','Bsc ','Computer science','NIL','NIL','2023','kowsalyakannan29@gmail.com','kowsalyaai01@gmail.com','26/1, College road,Sri Ram theatre near, Musiri,Trichy(Dt)','Trichy','Kannan.A','Sundhari.K');
insert into srinidhi_details values(8,'Hajeera Sithika', 'Nil','L','1992-06-11',430341868981,41868981,8056447098,9751471799,8056447098,'TI2023F-C01E796','Password@123','BA','English','NIL','NIL','2013','hajeerasithka2021@gmail.com','hajeerasithikaai01@gmail.com','3, murugesan street, M.K.kottai,trichy','Trichy','Syed Azarudeen','Amthul jabeen');
insert into srinidhi_details values(9,'HARIHARAN','Nil',' A','2001-10-11',304765424440,65424440,9363649175,9363649175,9363649175,'PE2023M-C01E437','Password@123','BE','EEE','NIL','NIL','2023','hariharananbu2001@gmail.com','hariharanai01@gmail.com','2/225 North st keelapuliyur po KunnamtkPerambalur dt 621115','Perambalur','ANBALAGAN D','Anjalai A');
insert into srinidhi_details values(10,'Jayalakshmi', 'Nil','R','1997-02-06',432445616668,45616668,9500628375,6385632493,6385632493,'TI2023F-C01E444','Password@123','BCA','Computer application','MCA','Computer Application','2019','jasperjeevi@gmail.com','jayalakshmiai01@gmail.com','28-A, bharathiyar Street, west ambigapuram, trichy-4','Trichy','Ravikumar','Geetha');
insert into srinidhi_details values(11,'Jothika','Nil',' J','2003-01-08',693941180387,41180387,9585607631,9843412199,9585607631,'TI2023F-C01E555','Password@123','BSC','Mathematics','NIL','NIL','2023','jothikajagan8@gmail.com','jothikaai01@gmail.com','H/5, Housing Unit, Parvathipuram, Musiri, Trichy DT.','Trichy','Jegatharatchagan K','Manjula J');
insert into srinidhi_details values(12,'Kalaiarasan' ,'Nil','A','1987-7-29',447595386464,95386464,9600330846,9994057344,9600330846,'TI2023M-C01E78B','Password@123','B.com','Commerce','NIL','NIL','2009','Kalai29.7@gmail.com','kalairasanai01@gmail.com','2/337 navalpattu burma colony oft po trichy 16','Trichy','K.Ayyavoo','A.Vasanthi');
insert into srinidhi_details values(13,'Kayalvizhi','Nil',' M','1998-09-13',7339221973,7339221973,9698821473,7339221973,9698821473,'TI2023F-C01E475','Password@123','BE','Mechanical engineering','NIL','NIL','2020','kayalmahe123@gmail.com','kayalai01@gmail.com','Door No: 2/125A, Koothur colony, Koothur post, mannachanallur Tk, Trichy - 621216','Trichy','Mahendhran.N','Vijayaragini .M');
insert into srinidhi_details values(14,'Komaladevi','Nil',' S','2003-07-29',460205744637,05744637,8940898862,7904257743,8940898862,'PU2023F-C01E466','Password@123','BSC','Computer science','NIL','NIL','2023','komaladevi2003@gmail.com','komaladeviai01@gmail.com','Gandharvakkottai pudukottai','Pudukottai','M. Subramaniyan','Kalaiselvi. S');
insert into srinidhi_details values(15,'LAVANYA ','Nil','M ','2001-02-26',629731226643,31226643,7904460924,8248554770,7904460924,'TI2023F-C01EA43','Password@123','BSC ','Mathematics','NIL','NIL','2021','mlavanyam37@gmail.com','lavanyaai01@gmail.com','33/66 Kamala Nehru Nagar, EB Road','Trichy','Aravind samy R','Avadaiyammal');
insert into srinidhi_details values(16,'Narayanan','Nil',' S','1999-06-14',282903912214,03912214,9361015928,8122648085,9361015928,'TI2023M-C01E78C','Password@123','BA','History','NIL','NIL','2019','Naveenkds82@gmail.com','narayananai01@gmail.com','3/141 Sivan kovil street allithurai somarampettai post trichy 620102','Trichy','Sivaprakasam','Sumathi');
insert into srinidhi_details values(17,'Prasanth','Nil', 'P','2000-07-27',983315540255,15540255,9361216766,9626922317,9361216766,'PU2023M-C01E445','Password@123','BE','ECE','NIL','NIL','2022','aryanprasanth163@gmail.com','prasanthai01@gmail.com','No 105, Maruthampatti, Vilapatti(post), Ilupur (Taluk), Pudukkottai-622504','Pudukkottai','Palanisamy M','Ponnazhagu P');
insert into srinidhi_details values(18,'Priya','nil', 'S','2002-05-05',920343048388,43048388,9626940557,9626940557,8508332712,'TI2023F-C01EC0E','Password@123','B.SC','Physics','NIL','NIL','2023','lakshmipriya5522@gmail.com','priyaai01@gmail.com','10,Mettu street,Wouraiyur Trichy-3','Trichy','SenthilKumar M','Elangiyam S');
insert into srinidhi_details values(19,'Punithavathi','Nil',' D','1997-05-22',762578126673,78126673,6369782863,9715451286,6369782863,'TI2023F-C01E8C2','Password@123','B.Com','Commerce','NIL','NIL','2025','Punithavathid1997@gmail.com','punithaai01@gmail.com','2/275,NPS colony,OFT Main Road, HAPF Town, Suriyur Post, Trichy-620025','Trichy','V. Devaraj','D. Santhamani');
insert into srinidhi_details values(20,'Raghul','Nil','S','2000-06-07',871736862600,871736862600,36862600,7010107069,8680827179,'TI2023M-C01E4E6','Password@123','BE','MECHANICAL ENGINEERING','NIL','NIL','2023','rockstarraghul55@gmail.com','ragulai01@gmail.com','3/443 mgr rajaveethi Vs colony Kattur Trichy 620019','Trichy','Senthil Kumar p','Sumathi S');
insert into srinidhi_details values(21,'Roobankumar','Nil','K','1992-11-22',612231264958,31264958,7904255453,9486645960,7904255453,'TI2023M-C01E8CB','Password@123','BE','ECE','NIL','NIL','2015','vroobank92@gmail.com','roobankumarai01@gmail.com','L1, chandradhayam, Shankar abodes, near kr motors, chennai trunk road, Thiruvanaikovil, trichy','Trichy','Kumaravel','Valli');
insert into srinidhi_details values(22,'Sangari','Nil',' S','1998-01-19',360158896738,58896738,9787264394,9751721397,9787264394,'TH2023F-C01E43E','Password@123','BE','ECE','NIL','NIL','2019','sangarisaminathan@gmail.com','sangariai01@gmail.com','1/44, Agraharam, North budalur, Thanjavur (Dt),613602','Thanjavur','Saminathan M','Latha S');
insert into srinidhi_details values(23,'Santhiya','Nil',' S','2003-04-29',842296226066,96226066,8940937523,9842021095,8940937522,'TI2023F-C01E43D','Password@123','Bsc ','Information technology','NIL','NIL','2023','santhiyasakthivel37@gmail.com','snthiyaai01@gmail.com','No 57,3rd street gandhinagar, college road musiri, trichy(dt)','Trichy','Sakthivel.T','Chitra S');
insert into srinidhi_details values(24,'Saranya','Nil',' N','1994-07-28',971123726105,23726105,8248879007,9585031787,8248879007,'TI2023F-C01EA19','Password@123','BE','CSE','NIL','NIL','2015','saranyanarayananai01@gmail.com','saranyaai01@gmail.com','No3a Balaji Avenue 1st cross, Old karur road, Melachinthamani Trichy 620002','Trichy','S.Narayanan','A.Marikkannu');
insert into srinidhi_details values(25,'Saravanan','Nil','M','2003-05-20',385868916470,68916470,8838011266,7603972485,8838011266,'TH2023M-C01E44A','Password@123','BSC','Computer Science','NIL','NIL','2023','saravanasaro1435@gmail.com','saravanamaiai01@gmail.com','1/88, Vallabramankadu, Sornakadu (Post), Peravurani(Taluk), Thanjavur (District)-614804','Thanjavur','Malaiyarasan V','Ganamani M');
insert into srinidhi_details values(26,'Snega','Nil','D','2003-04-05',546307861816,07861816,9047648856,8072885475,9047648856,'TI2023F-C01E446','Password@123','BSC','IT','NIL','NIL','2023','Stdsnega.it@cauverycollege.ac.in','snegadai01@gmail.com','1-130 / A perumal Kovil street, Reddi mangudi, Trichy','Trichy','R.Durai raj','D.Bhuvaneswari');
insert into srinidhi_details values(27,'Srinidhi','Nil','S','2001-12-19',733557069525,57069525,9360728585,9500868943,9360728585,'TI2023F-C01EA34','Password@123','BSC','IT','NIL','NIL','2023','Srinidhisrinidhi233@gmail.com','srinidhiai01@gmail.com','45/B East street, melur, srirangam','Trichy','Sundarrajan B','Shanthi. S');
insert into srinidhi_details values(28,'Tamil','Nil','v','2003-05-09',277289901567,89901567,7904761471,7904761471,7904761471,'TI2023F-C01EA44','Password@123','BSC','IT','NIL','NIL','2023','venktesantamil@gmail.com','tamilvai01@gmail.com','45/B East street, Melur, Srirangam, Trichy','Trichy','Venktesan B','Lalitha V');
insert into srinidhi_details values(29,'Vinu Andrews','Nil',' S','1999-11-24',543353698598,543353698598,53698598,8428908488,8428908488,'TI2023M-C01F2A8','Password@123','Bba','business administration','MBA','Safety','2022','vinuandrews10@gmail.com','vinuandrewsai01@gmail.com','66, muslim street varaganeri Trichy','Trichy','Selvaraj A','Mercy s');
insert into srinidhi_details values(30,'Yogarajan','Nil',' K','2001-12-15',241602457541,02457541,6379275571,8056724735,6379275571,'TH2023M-C01E455','Password@123','BCA','Computer Application','NIL','NIL','2022','yogiraja2001@gmail.com','yogarajanai01@gmail.com','44,agraharam,north Budalur, Budalur, Thanjavur (dt).Pincode:613602','Thanjavur','M.Kaliyamoorthy','K.Uma maheswari');

