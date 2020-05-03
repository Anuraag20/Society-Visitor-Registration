create table visitors

(
v_code bigint(8) primary key not null auto_increment,
f_name varchar(25) not null,
l_name varchar(25) not null,
mobile bigint(11) not null,
address varchar(100) not null,
wing varchar(2) not null,
flat int(5) not null,
purpose varchar(50) not null,
company_name varchar(30) default 'NULL',
cin_d varchar(12) not null,
cin_t varchar(12) not null,
cout_d varchar(12) default 'NULL',
cout_t varchar(12) default 'NULL',
watchman_code bigint(6) not null 
);

alter table visitors auto_increment=1000;


--------------------------------------------------------------------------------------
create table employee
(
employee_code bigint(6) primary key not null auto_increment,
e_firstname varchar(25) not null,
e_lastname varchar(25) not null,
e_address varchar(100) not null,
e_mobile bigint(20) not null,
e_birthday varchar(20) not null,
e_joindate varchar(20) not null,
e_designation varchar(20) not null
);

alter table employee auto_increment=50000;

--------------------------------------------------------------------------------------
create table emp_att
(
sr_no int(3) primary key not null auto_increment,
employee_code bigint(6) not null,
ecin_d varchar(12) not null,
ecin_t varchar(12) not null,
ecout_d varchar(12) default 'NULL',
ecout_t varchar(12) default 'NULL'
); 
--------------------------------------------------------------------------------------

create table passwords
(
employee_code bigint(6) primary key auto_increment,
passwd varchar(25) not null,
foreign key (employee_code) references employee(employee_code)
);

alter table passwords auto_increment=50000;

