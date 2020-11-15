import os, sys
import functions as function
import init as init

def check_already_exists():
    Cursor = init.DB_con.cursor()
    Cursor.execute("SHOW TABLES")
    LC = [x[0] for x in Cursor if "Tracks" in x]
    if 'Tracks' in LC:
        return True
    else:
        return False

def create_Tables():
    Cursor = init.DB_con.cursor()
    Cursor.execute("CREATE TABLE IF NOT EXISTS `Artists` ( `ID` int(11) NOT NULL AUTO_INCREMENT, `Name` char(100) NOT NULL DEFAULT '', `Alias` char(100) NOT NULL DEFAULT '', PRIMARY KEY (`ID`) ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;")
    Cursor.execute("CREATE TABLE IF NOT EXISTS `Tracks` ( `ID` int(11) NOT NULL AUTO_INCREMENT, `Title` char(150) NOT NULL DEFAULT '', `Date_Added` datetime DEFAULT NULL,  `by_Artist1` int(11) DEFAULT 0, `by_Artist2` int(11) DEFAULT 0,`by_Artist3` int(11) DEFAULT 0,  PRIMARY KEY (`ID`),  KEY `FK_Tracks_Artists` (`by_Artist1`),  KEY `FK_Tracks_Artists_2` (`by_Artist2`),  KEY `FK_Tracks_Artists_3` (`by_Artist3`)) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;")
    Cursor.execute("CREATE TABLE IF NOT EXISTS `Version` (  `ver` int(11) DEFAULT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;")
    Cursor.execute("INSERT INTO `Version` (`ver`) VALUES ('1');")

