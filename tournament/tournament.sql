-- Set up tournament database for project 2
--
-- To run this file, connect to psql from the command
-- line, and enter \i tournament.sql to import it.
--
-- More detailed instructions can be found in README.md.



-- Create tournament database, and connect to it
--
-- Drop the database if it already exists first.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.


