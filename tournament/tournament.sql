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
-- already does that :)



-- Create the players table

CREATE TABLE players (
  player_id smallserial PRIMARY KEY,
  name text
);

-- Create the matches table

CREATE TABLE matches (
  winner_id smallint REFERENCES players,
  loser_id smallint REFERENCES players,
  PRIMARY KEY (winner_id, loser_id)
);

-- Create a playerwins view

CREATE VIEW playerwins AS
    SELECT p.player_id, count(m.winner_id) AS wins
    FROM players AS p
        LEFT OUTER JOIN matches AS m ON (p.player_id = m.winner_id)
    GROUP BY p.player_id
    ORDER BY wins DESC;

-- Create a playermatches view

CREATE VIEW playermatches AS
    SELECT p.player_id, count(m.winner_id) AS num_matches
    FROM players AS p, matches as m
    WHERE p.player_id = m.winner_id OR p.player_id = m.loser_id
    GROUP BY p.player_id;


-- Create a playerstandings view

CREATE VIEW playerstandings AS
    SELECT p.player_id, p.name, w.wins, m.num_matches
    FROM players AS p
        LEFT OUTER JOIN playerwins AS w ON(p.player_id = w.player_id)
        LEFT OUTER JOIN playermatches AS m ON(p.player_id = m.player_id)
    ORDER BY w.wins DESC;
