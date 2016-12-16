--------------------------------------------------------------------------------
--            Fjöldi dauðsfalla af völdum lögreglu á hverju phasei.
select (select count(time)
        from fatalpoliceshootings
        where time in (select time
                       from moons
                       where phase = 'Full Moon')) as "Full Moon",
        (select count(time)
        from fatalpoliceshootings
        where time in (select time
                       from moons
                       where phase = 'New Moon')) as "New Moon",
        (select count(time)
        from fatalpoliceshootings
        where time in (select time
                       from moons
                       where phase = 'First Quarter')) as "First Quarter",
        (select count(time)
        from fatalpoliceshootings
        where time in (select time
                       from moons
                       where phase = 'Last Quarter')) as "Last Quarter";

--Count þegar það er ekki fullt, nýtt eða hálft tungl (hægt að taka síðan hvað sem er í burtu)
select count(time)
from emergencycalls
where time not in (select time
                   from moons
                   where phase = 'Full Moon'
                   or phase = 'New Moon'
                   or phase = 'First Quarter'
                   or phase = 'Last Quarter');

--------------------------------------------------------------------------------
--              Fjöldi glæpa á phasei raðað í stærðarröð
select offense, count(offense_id)/186
from crimes, offenses
where offenses.id = crimes.offense_id
and crimes.time in (select time
                    from moons
                    where phase like 'Full Moon')
group by offenses.offense
order by count(offense_id) desc;
--Fyrir 1 venjulegan dag:
select offense, count(offense_id)/5401
from crimes, offenses
where offenses.id = crimes.offense_id
and crimes.time not in (select time
                    from moons
                    where phase like 'Full Moon')
group by offenses.offense
order by count(offense_id) desc;


select offense, count(offense_id)/186
from crimes, offenses
where offenses.id = crimes.offense_id
and crimes.time in (select time
                    from moons
                    where phase like 'New Moon')
group by offenses.offense
order by count(offense_id) desc;
--Fyrir 1 venjulegan dag:
select offense, count(offense_id)/5401
from crimes, offenses
where offenses.id = crimes.offense_id
and crimes.time not in (select time
                    from moons
                    where phase like 'New Moon')
group by offenses.offense
order by count(offense_id) desc;


select offense, count(offense_id)/186
from crimes, offenses
where offenses.id = crimes.offense_id
and crimes.time in (select time
                    from moons
                    where phase like 'First Quarter')
group by offenses.offense
order by count(offense_id) desc;
--Fyrir 1 venjulegan dag:
select offense, count(offense_id)/5401
from crimes, offenses
where offenses.id = crimes.offense_id
and crimes.time not in (select time
                    from moons
                    where phase like 'First Quarter')
group by offenses.offense
order by count(offense_id) desc;


select offense, count(offense_id)/186
from crimes, offenses
where offenses.id = crimes.offense_id
and crimes.time in (select time
                    from moons
                    where phase like 'Last Quarter')
group by offenses.offense
order by count(offense_id) desc;
--Fyrir 1 venjulegan dag:
select offense, count(offense_id)/5401
from crimes, offenses
where offenses.id = crimes.offense_id
and crimes.time not in (select time
                    from moons
                    where phase like 'Last Quarter')
group by offenses.offense
order by count(offense_id) desc;

--Fjöldi glæpa ekki á phasei raðað í stærðarröð (hægt að taka síðan hvað sem er í burtu)

select offense, count(offense_id)
from crimes, offenses
where offenses.id = crimes.offense_id
and crimes.time not in (select time
                   from moons
                   where phase = 'Full Moon'
                   or phase = 'New Moon'
                   or phase = 'First Quarter'
                   or phase = 'Last Quarter')
group by offenses.offense
order by count(offense_id) desc;


--------------------------------------------------------------------------------
--             Hversu margir glaepir voru framdir a phasei.
select (select count(offense_id)
from crimes
where time in (select time
               from moons
               where phase like 'New Moon')) as "New Moon",
(select count(offense_id)
from crimes
where time in (select time
               from moons
               where phase like 'Full Moon')) as "Full Moon",
(select count(offense_id)
from crimes
where time in (select time
               from moons
               where phase like 'First Quarter')) as "First Quarter",
(select count(offense_id)
from crimes
where time in (select time
               from moons
               where phase like 'Last Quarter')) as "Last Quarter";


--BÚA TIL TÖFLU ÚR ÞESSU:
select (select count(offense_id)/186
from crimes
where time in (select time
              from moons
              where phase like 'New Moon')) as "New Moon",
(select count(offense_id)/186
from crimes
where time in (select time
              from moons
              where phase like 'Full Moon')) as "Full Moon",
(select count(offense_id)/186
from crimes
where time in (select time
              from moons
              where phase like 'First Quarter')) as "First Quarter",
(select count(offense_id)/186
from crimes
where time in (select time
              from moons
              where phase like 'Last Quarter')) as "Last Quarter",
(select count(offense_id)/5401
from crimes
where time not in (select time
              from moons
              where phase like 'New Moon')) as "Normal Day";

--Count þegar það er ekki fullt, nýtt eða hálft tungl (hægt að taka síðan hvað sem er í burtu)
select count(offense_id)
from crimes
where time not in (select time
                  from moons
                  where phase = 'Full Moon'
                  or phase = 'New Moon'
                  or phase = 'First Quarter'
                  or phase = 'Last Quarter');


--------------------------------------------------------------------------------
--              Mest framdi glæpurinn eftir öllum phaseum
--select offense, count(offense_id)
--from crimes, offenses
--where offenses.id = crimes.offense_id
--and crimes.time in (select time
--                    from moons
--                    where phase like 'Full Moon')
--group by offenses.offense
--order by count(offense_id) desc;

--select count(offense_id)
--from crimes
--where crimes.offense_id = 1784456

--select count(*) as fullmoon
--from fatalpoliceshootings
--where fatalpoliceshootings.time in (select time
--                                    from moons
--                                    where moons.phase = 'Full Moon')
--select count(*) as Newmoon
--from fatalpoliceshootings
--where fatalpoliceshootings.time in (select time
--                                    from moons
--                                    where moons.phase = 'New Moon')

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
--Eru fleiri simtol i 911 a fullu tungli?
select (select count(time)
        from emergencyCalls
        where emergencyCalls.time in (select time
                                       from moons
                                      where moons.phase = 'Full Moon')) as "Full Moon",
        (select count(time)
        from emergencyCalls
        where emergencyCalls.time in (select time
                                      from moons
                                      where moons.phase = 'New Moon')) as "New Moon",
        (select count(time)
        from emergencyCalls
        where emergencyCalls.time in (select time
                                      from moons
                                      where moons.phase = 'First Quarter')) as "First Quarter",
        (select count(time)
        from emergencyCalls
        where emergencyCalls.time in (select time
                                      from moons
                                      where moons.phase = 'Last Quarter')) as "Last Quarter";

--Count þegar það er ekki fullt, nýtt eða hálft tungl (hægt að taka síðan hvað sem er í burtu)
select count(time)
from emergencyCalls
where time not in (select time
                from moons
                where phase = 'Full Moon'
                or phase = 'New Moon'
                or phase = 'First Quarter'
                or phase = 'Last Quarter');

--Eru fleiri glæpir framdir á fullu tungli?
select (select count(time)
        from crimes
        where crimes.time in (select time
                              from moons
                              where moons.phase = 'Full Moon')) as "Full Moon",
        (select count(time)
        from crimes
        where crimes.time in (select time
                              from moons
                              where moons.phase = 'New Moon')) as "New Moon",
        (select count(time)
        from crimes
        where crimes.time in (select time
                              from moons
                              where moons.phase = 'First Quarter')) as "First Quarter",
        (select count(time)
        from crimes
        where crimes.time in (select time
                              from moons
                              where moons.phase = 'Last Quarter')) as "Last Quarter";

--Count þegar það er ekki fullt, nýtt eða hálft tungl (hægt að taka síðan hvað sem er í burtu)
select count(time)
from crimes
where time not in (select time
              from moons
              where phase = 'Full Moon'
              or phase = 'New Moon'
              or phase = 'First Quarter'
              or phase = 'Last Quarter');

--Eru fleiri dauðsföll af völdum lögreglunnar á fullu tungli?
-- SAMA OG UPPI!---------------------------------------------
select (select count(time)
        from fatalpoliceshootings
        where fatalpoliceshootings.time in (select time
                                            from moons
                                            where moons.phase = 'Full Moon')) as "Full Moon",
        (select count(time)
        from fatalpoliceshootings
        where fatalpoliceshootings.time in (select time
                                            from moons
                                            where moons.phase = 'New Moon')) as "New Moon",
        (select count(time)
        from fatalpoliceshootings
        where fatalpoliceshootings.time in (select time
                                            from moons
                                            where moons.phase = 'First Quarter')) as "First Quarter",
        (select count(time)
        from fatalpoliceshootings
        where fatalpoliceshootings.time in (select time
                                            from moons
                                            where moons.phase = 'Last Quarter')) as "Last Quarter";


-- Eru fleiri sem deyja af völdum eiturlyfja á fullu tungli?
select (select count(sex)
        from drugdeaths
        where lower(sex) like 'male'
        and drugdeaths.time in (select time
                                from moons
                                where moons.phase = 'Full Moon')) as "Male Deaths on Full moon",
        (select count(sex)
        from drugdeaths
        where lower(sex) like 'female'
        and drugdeaths.time in (select time
                                from moons
                                where moons.phase = 'Full Moon')) as "Female Deaths on Full moon",
        (select count(sex)
        from drugdeaths
        where lower(sex) like 'male') as "Male Deaths overall",
        (select count(sex)
        from drugdeaths
        where lower(sex) like 'female') as "Female Deaths overall";


-- Hversu margir dóu af hvaða orsök af völdum eiturlyfja
select count(cause), cause
from drugdeaths
where time in (select time
               from moons
               where phase = 'Full Moon')
group by cause
order by count(cause) desc;


select count(cause), cause
from drugdeaths
where time in (select time
               from moons
               where phase = 'New Moon')
group by cause
order by count(cause) desc;


select count(cause), cause
from drugdeaths
where time in (select time
               from moons
               where phase = 'First Quarter')
group by cause
order by count(cause) desc;


select count(cause), cause
from drugdeaths
where time in (select time
               from moons
               where phase = 'Last Quarter')
group by cause
order by count(cause) desc;

-- Hversu margir dóu af hvaða orsaki af völdum eiturlyfja EKKI phase
select count(cause), cause
from drugdeaths
where time not in (select time
              from moons
              where phase = 'Full Moon'
              or phase = 'New Moon'
              or phase = 'First Quarter'
              or phase = 'Last Quarter')
group by cause
order by count(cause) desc;



-- Hversu margir af hverjum kynþætti dóu af völdum eiturlyfja á hverju phasei.
select count(race), race
from drugdeaths
where time in (select time
                from moons
                where moons.phase = 'Full Moon')
group by race
order by count(race) desc;


select count(race), race
from drugdeaths
where race in (select race
               from moons
               where moons.phase = 'New Moon')
group by race
order by count(race) desc;


select count(race), race
from drugdeaths
where time in (select time
               from moons
               where phase = 'First Quarter')
group by race
order by count(race) desc;


select count(race), race
from drugdeaths
where time in (select time
               from moons
               where phase = 'Last Quarter')
group by race
order by count(race) desc;

-- Hversu margir af hverjum kynþætti dóu af völdum eiturlyfja EKKI á hverju phasei
select count(race), race
from drugdeaths
where time not in (select time
              from moons
              where phase = 'Full Moon'
              or phase = 'New Moon'
              or phase = 'First Quarter'
              or phase = 'Last Quarter')
group by race
order by count(race) desc;

-- Hversu margir deyja af völdum eiturlyja eftir hverju eiturlyfi.
select count(lower(cause)), lower(cause)
from drugdeaths
group by cause
order by count(cause) desc;

-- Hversu margir deyja af völdum eiturlyja eftir hverju eiturlyfi EKKI á phasei.

select count(lower(cause)), lower(cause)
from drugdeaths
where time not in (select time
              from moons
              where phase = 'Full Moon'
              or phase = 'New Moon'
              or phase = 'First Quarter'
              or phase = 'Last Quarter')
group by cause
order by count(cause) desc;


-- Hversu margir deyja af völdum eiturlyfja á hverju phasei.
select (select count(time)
        from drugdeaths
        where drugdeaths.time in (select time
                                  from moons
                                  where moons.phase = 'Full Moon')) as "Full Moon",
        (select count(time)
        from drugdeaths
        where drugdeaths.time in (select time
                                   from moons
                                   where moons.phase = 'New Moon')) as "New Moon",
        (select count(time)
        from drugdeaths
        where drugdeaths.time in (select time
                                   from moons
                                   where moons.phase = 'First Quarter')) as "First Quarter",
        (select count(time)
        from drugdeaths
        where drugdeaths.time in (select time
                                   from moons
                                   where moons.phase = 'Last Quarter')) as "Last Quarter";

--------------------------------------------------------------------------------
--                TOP 3 Borgir með flest dauðsföll af völdum lögreglu
select cities.city, count(fatalpoliceshootings.time)
from cities, fatalpoliceshootings
where cities.id = fatalpoliceshootings.city_id
group by cities.city
order by count(fatalpoliceshootings.time) desc
limit 3;

--------------------------------------------------------------------------------
--            TOP 3 Borgir með flest dauðsföll af völdum eiturlyfja
select cities.city, count(drugdeaths.time)
from cities, drugdeaths
where cities.id = drugdeaths.city_id
group by cities.city
order by count(drugdeaths.time) desc
limit 3;

--------------------------------------------------------------------------------
--      Hvaða borgir voru bæði með dauðsföll af völdum lögreglu og eiturlyfja
-- ÞETTA VIRKAR EKKI
select cities.city, count(fatalpoliceshootings.time) as "Fatal Deaths", count(drugdeaths.time) as "Drug Deaths"
from cities, fatalpoliceshootings, drugdeaths
where cities.id = fatalpoliceshootings.city_id
and cities.id = drugdeaths.city_id
group by cities.city

--------------------------------------------------------------------------------
--         Borgir með fjölda dauðsfalla af völdum lögreglu og eiturlyja
select cities.city, drugdeath.count as "Drugdeaths", policedeaths.count as "Policedeaths"
from cities, (select count(drugdeaths.time), cities.city
        from cities, drugdeaths
        where drugdeaths.city_id = cities.id
        group by cities.city) as drugdeath
  full join
        (select count(fatalpoliceshootings.time), cities.city
        from cities, fatalpoliceshootings
        where fatalpoliceshootings.city_id = cities.id
        group by cities.city) as policedeaths
on drugdeath.city = policedeaths.city
where cities.city = policedeaths.city or cities.city = drugdeath.city
group by cities.city, drugdeath.count, policedeaths.count;
