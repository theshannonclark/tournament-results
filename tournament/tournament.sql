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



-- Table definitions for the tournament project
--
-- Two tables: players and matches. No need to
-- drop them first, since dropping the database
-- already does that.



-- Create the players table

CREATE TABLE players (
  player_id smallserial PRIMARY KEY,
  first_name text,
  last_name text
);

-- Create the matches table

CREATE TABLE matches (
  p1_id smallint REFERENCES players,
  p2_id smallint REFERENCES players,
  winner_id smallint REFERENCES players,
  PRIMARY KEY (p1_id, p2_id)
);
