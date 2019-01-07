/* Create Stock Table and Sequence  */
create table stock (s_id int primary key, price float, read_time varchar(256), stock_name varchar(256), stock_symbol varchar(256));
create sequence stock_id_sequence start with 1 increment by 1;

/* Drop Stock Table and Sequence */
drop table stock;
drop sequence stock_id_sequence;
