--Eru fleiri simtol i 911 a fullu tungli?
select (select count(*)
        from emergencyCalls
        where emergencyCalls.time in (select time
                         from moons
                          where moons.phase = 'Full Moon')) as "Full Moon",
        (Select count(*)
        from emergencyCalls
         where emergencyCalls.time in (select time
                           from moons
                           where moons.phase = 'New Moon')) as "New Moon",
        (Select count(*)
        from emergencyCalls
         where emergencyCalls.time in (select time
                           from moons
                           where moons.phase = 'First Quarter')) as "First Quarter",
        (Select count(*)
        from emergencyCalls
         where emergencyCalls.time in (select time
                           from moons
                           where moons.phase = 'Last Quarter')) as "Last Quarter";


--Eru fleiri glæpir framdir á fullu tungli?
select (select count(*)
        from crimes
        where crimes.time in (select time
                         from moons
                          where moons.phase = 'Full Moon')) as "Full Moon",
        (Select count(*)
        from crimes
         where crimes.time in (select time
                           from moons
                           where moons.phase = 'New Moon')) as "New Moon",
        (Select count(*)
        from crimes
         where crimes.time in (select time
                           from moons
                           where moons.phase = 'First Quarter')) as "First Quarter",
        (Select count(*)
        from crimes
         where crimes.time in (select time
                           from moons
                           where moons.phase = 'Last Quarter')) as "Last Quarter";

--Hvaða glæpir eru algengastir á  fullu tungli?
SELECT avg(offense_id), offense FROM crimes, offenses WHERE offenses.id = crimes.offense_id AND crimes.time in (SELECT time FROM moons WHERE phase LIKE 'Full Moon') GROUP BY offenses.offense;
SELECT avg(offense_id), offense FROM crimes, offenses WHERE offenses.id = crimes.offense_id GROUP BY offenses.offense;

--Eru fleiri dauðsföll af völdum lögreglunnar á fullu tungli?
select (select count(*)
        from fatalpoliceshootings
        where fatalpoliceshootings.time in (select time
                          from moons
                          where moons.phase = 'Full Moon')) as "Full Moon",
        (Select count(*)
        from fatalpoliceshootings
         where fatalpoliceshootings.time in (select time
                           from moons
                           where moons.phase = 'New Moon')) as "New Moon",
        (Select count(*)
        from fatalpoliceshootings
         where fatalpoliceshootings.time in (select time
                           from moons
                           where moons.phase = 'First Quarter')) as "First Quarter",
        (Select count(*)
        from fatalpoliceshootings
         where fatalpoliceshootings.time in (select time
                           from moons
                           where moons.phase = 'Last Quarter')) as "Last Quarter";


-- Eru fleiri sem deyja af völdum eiturlyfja á fullu tungli?
select (select count(sex)
        from drugdeaths
        where lower(sex) LIKE 'male' AND drugdeaths.time in (select time
                          from moons
                          where moons.phase = 'Full Moon')) as "Male Deaths on Full moon",
        (select count(sex)
        from drugdeaths
        where lower(sex) LIKE 'female' AND drugdeaths.time in (select time
                          from moons
                          where moons.phase = 'Full Moon')) as "Female Deaths on Full moon",
        (select count(sex)
        from drugdeaths
        where lower(sex) LIKE 'male') as "Male Deaths overall",
        (select count(sex)
        from drugdeaths
        where lower(sex) LIKE 'female') as "Female Deaths overall";



SELECT count(cause), cause FROM drugdeaths WHERE time in (select time
                           from moons
                           where moons.phase = 'Full Moon') GROUP BY cause ORDER BY count(cause) DESC;
SELECT count(cause), cause FROM drugdeaths WHERE time in (select time
                           from moons
                           where moons.phase = 'New Moon') GROUP BY cause ORDER BY count(cause) DESC;
SELECT count(cause), cause FROM drugdeaths WHERE time in (SELECT time
                           from moons WHERE phase = 'First Quarter') GROUP BY cause ORDER BY count(cause) DESC;
SELECT count(cause), cause FROM drugdeaths WHERE time in (SELECT time
                           from moons WHERE phase = 'Last Quarter') GROUP BY cause ORDER BY count(cause) DESC;




SELECT count(race), race FROM drugdeaths WHERE time in (select time
                           from moons
                           where moons.phase = 'Full Moon') GROUP BY race ORDER BY count(race) DESC;
SELECT count(race), race FROM drugdeaths WHERE race in (select race
                           from moons
                           where moons.phase = 'New Moon') GROUP BY race ORDER BY count(race) DESC;
SELECT count(race), race FROM drugdeaths WHERE time in (SELECT time
                           from moons WHERE phase = 'First Quarter') GROUP BY race ORDER BY count(race) DESC;
SELECT count(race), race FROM drugdeaths WHERE time in (SELECT time
                           from moons WHERE phase = 'Last Quarter') GROUP BY race ORDER BY count(race) DESC;

SELECT count(lower(cause)), lower(cause) FROM drugdeaths GROUP BY cause ORDER BY count(cause) DESC;

select (select count(*)
        from drugdeaths
        where drugdeaths.time in (select time
                          from moons
                          where moons.phase = 'Full Moon')) as "Full Moon",
        (Select count(*)
        from drugdeaths
         where drugdeaths.time in (select time
                           from moons
                           where moons.phase = 'New Moon')) as "New Moon",
        (Select count(*)
        from drugdeaths
         where drugdeaths.time in (select time
                           from moons
                           where moons.phase = 'First Quarter')) as "First Quarter",
        (Select count(*)
        from drugdeaths
         where drugdeaths.time in (select time
                           from moons
                           where moons.phase = 'Last Quarter')) as "Last Quarter";
