create table moons (
	id serial,
	phase varchar (250),
	time timestamp,
	primary key (id)
);

create table crimes (
 id serial,
 time int,
 offense varchar(50),
 method varchar (50),
 primary key (id)
);

create table emergencyCalls (
	id serial,
	time int,
	address varchar(250),
	primary key (id)
);
