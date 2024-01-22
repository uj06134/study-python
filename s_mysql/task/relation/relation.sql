create table tbl_parent(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    age tinyint default 1,
    gender varchar(255) not null,
    address varchar(255) not null,
    phone varchar(255) not null,
    constraint check_gender check ( gender in ('선택안함', '여자', '남자') )
);

create table tbl_child(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    age tinyint default 1,
    gender varchar(255) not null,
    parent_id bigint not null,
    constraint check_child_gender check ( gender in ('선택안함', '여자', '남자') ),
    constraint fk_child_parent foreign key (parent_id)
                      references tbl_parent(id)
);

create table tbl_field_trip(
    id bigint auto_increment primary key,
    title varchar(255) not null,
    content varchar(255) not null,
    count tinyint default 0
);

create table tbl_file(
    /* 슈퍼키 */
    id bigint auto_increment primary key,
    file_path varchar(255) not null,
    file_name varchar(255) not null
);

create table tbl_field_trip_file(
    /* 서브키 */
    id bigint primary key,
    field_trip_id bigint not null,
    constraint fk_field_trip_file_file foreign key (id)
    references tbl_file(id),
    constraint fk_field_trip_file_field_trip foreign key (field_trip_id)
    references tbl_field_trip(id)
);

create table tbl_apply(
    id bigint auto_increment primary key,
    child_id bigint not null,
    field_trip_id bigint not null,
    constraint fk_apply_child foreign key (child_id)
    references tbl_child(id),
    constraint fk_apply_field_trip foreign key (field_trip_id)
    references tbl_field_trip(id)
);

select * from tbl_parent;
select * from tbl_child;
select * from tbl_field_trip;
select * from tbl_file;
select * from tbl_field_trip_file;

##############################################################

create table tbl_user(
    id bigint auto_increment primary key,
    user_id varchar(255) not null unique,
    password varchar(255) not null,
    name varchar(255) not null,
    address varchar(255) not null,
    email varchar(255),
    birth date
);

create table tbl_post(
    id bigint auto_increment primary key,
    title varchar(255) not null,
    content varchar(255) not null,
    create_date datetime default current_timestamp,
    user_id bigint not null,
    constraint fk_post_user foreign key(user_id)
                     references tbl_user(id)
);

create table tbl_reply(
    id bigint auto_increment primary key,
    content varchar(255) not null,
    user_id bigint not null,
    post_id bigint not null,
    constraint fk_reply_user foreign key(user_id)
                     references tbl_user(id),
    constraint fk_reply_post foreign key(post_id)
                     references tbl_post(id)
);

select * from tbl_user;
select * from tbl_post;
select * from tbl_reply;

##############################################################

create table tbl_owner(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    age int default 0,
    phone varchar(255) not null,
    address varchar(255) not null
);

create table tbl_pet(
    id bigint auto_increment primary key,
    name varchar(255) default '사랑',
    ill_name varchar(255) not null,
    age int default 0,
#     weight decimal(1, 2) default 0.0,
    weight double default 0.0,
    owner_id bigint,
    constraint fk_pet_owner foreign key(owner_id)
                references tbl_owner(id)
);

select * from tbl_owner;
select * from tbl_pet;

##############################################################

create table tbl_client(
    email varchar(255) primary key,
    password varchar(255) not null,
    name varchar(255) not null
);

create table tbl_office(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    location varchar(255) not null
);

create table tbl_conference_room(
    id bigint auto_increment primary key,
    office_id bigint not null,
    constraint fk_conference_room_office foreign key(office_id)
                                references tbl_office(id)
);

create table tbl_part_time(
    id bigint auto_increment primary key,
    time time not null,
    conference_room_id bigint not null,
    constraint fk_part_time_conference_room foreign key(conference_room_id)
                                references tbl_conference_room(id)
);

create table tbl_reservation(
    id bigint auto_increment primary key,
    time time not null,
    created_date datetime default (current_timestamp),
    client_email varchar(255) not null,
    conference_room_id bigint not null,
    constraint fk_reservation_client foreign key (client_email)
                            references tbl_client(email),
    constraint fk_reservation_conference_room foreign key (conference_room_id)
                            references tbl_conference_room(id)
);

select * from tbl_client;
select * from tbl_office;
select * from tbl_conference_room;
select * from tbl_part_time;
select * from tbl_reservation;





