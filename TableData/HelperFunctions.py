# Returns dictionary from table with table ID as a value and
# table data as value.
def getIds (table, cursor):
    select = "select * from " + table + ";"
    cursor.execute(select)
    records = cursor.fetchall()
    id_dict = {}
    for i in records:
        id_dict[i[1]] = i[0]
    return id_dict

def fixCities (s):
    return s.lower().title()

def fixOffense (s):
    return s.replace(' - ', '-')
