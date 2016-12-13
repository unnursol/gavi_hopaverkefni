create table moons (
	id serial,
	phase varchar (250),
	time int,
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

Create table fatalPoliceShootings (
	id serial,
	time int,
	causeOfDeath varchar(250),
	state varchar(250),
	city varchar(250),
	primary key(id)
);

create table drugDeaths (
    id serial,
    time int,
    sex varchar(20),
    age varchar(20),
    race varchar(250),
    cause varchar(250),
    deathcity varchar(250),
    primary key (id)
);
