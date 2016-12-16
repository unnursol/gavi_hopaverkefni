# Gagnavinnsla Hópaverkefni - Fullt tungl#
#### *Auður, Jóhanna, Sigrún og Unnur* ####

![picture alt](http://www.wheniscalendars.com/wp-content/uploads/2015/05/Full-Moon.jpg "Full Moon")

### Gögnin okkar ###
* Accidental drug related deaths 2012-2015
  https://catalog.data.gov/dataset/accidental-drug-related-deaths-january-2012-sept-2015
  
* Moon-phases 1970-2015
  http://www.somacon.com/p570.php
  
* Crimes from 2001-present
  https://catalog.data.gov/dataset/crimes-2001-to-present-398a4
  
* 911 Calls
  https://www.kaggle.com/mchirico/montcoalert
  
* Fatal police shootings
  https://www.kaggle.com/washingtonpost/police-shootings

### Leiðbeiningar ###
#### ./TableData ####
* CreateTable.sql inniheldur SQL fyrirspurnir sem býr til töflur fyrir gagnagrunninn okkar
* TableInit.py sér um alla innsetningu gagna frá csv skrám. TableInit notar hjálparskrárnar Connection.py, InsertFunctions.py og HelperFunctions.py

#### ./DataAccess ####
* SQL fyrirspurnir fyrir rannsóknarvinnuna. 
* Skipanir fyrir birtingu gagna (notuðum python safnið Plotly)
