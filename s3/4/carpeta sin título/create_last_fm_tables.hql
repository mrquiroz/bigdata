CREATE TABLE user_profile( user_mboxsha1 VARCHAR(100), gender VARCHAR(10), age INT, country VARCHAR(100), signup VARCHAR(100)) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';

LOAD DATA INPATH 'hdfs:///input1/user_profile' INTO TABLE user_profile; 

CREATE TABLE artists( user_mboxsha1 VARCHAR(100), musicbrainz_artist_id VARCHAR(10), artist_name VARCHAR(100), plays INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY ','; 

LOAD DATA INPATH 'hdfs:///input2/artists' INTO TABLE artists