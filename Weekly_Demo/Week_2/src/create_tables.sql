DROP DATABASE IF EXISTS go;
CREATE DATABASE go;

DROP TABLE IF EXISTS Taxi;
DROP TABLE IF EXISTS Covid;

\c go;

CREATE TABLE Taxi (
    ID SERIAL,
    PickupLoc FLOAT(10)
	DropLoc FLOAT(10)
);

CREATE TABLE Covid(
    Cases INT(4),
    WeekNum INT(2),
    Zip INT(5)
);