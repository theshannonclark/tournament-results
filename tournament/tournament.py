#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

class Tournament():

    def __init__(self):
        self.connection = None

    def __enter__(self):
        """ Connect to the database when using with statement. """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """ Disconnect from the database when leaving with statement. """
        self.close()

    def connect(self):
        """Connect to the PostgreSQL database.  Returns a database connection."""
        if not self.connection:
            self.connection = psycopg2.connect("dbname=tournament")

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def deleteMatches(self):
        """Remove all the match records from the database."""
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM matches;")
        self.connection.commit()

    def deletePlayers(self):
        """Remove all the player records from the database."""
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM players;")
        self.connection.commit()

    def countPlayers(self):
        """Returns the number of players currently registered."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT count(player_id) FROM players;")
        result_tuple = cursor.fetchone()
        num_players = result_tuple[0]

        return num_players


    def registerPlayer(self, name):
        """Adds a player to the tournament database.

        The database assigns a unique serial id number for the player.  (This
        should be handled by your SQL database schema, not in your Python code.)

        Args:
          name: the player's full name (need not be unique).
        """
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO players (name) VALUES (%s);", (name,))
        self.connection.commit()

    def playerStandings(self):
        """Returns a list of the players and their win records, sorted by wins.

        The first entry in the list should be the player in first place, or a player
        tied for first place if there is currently a tie.

        Returns:
          A list of tuples, each of which contains (id, name, wins, matches):
            id: the player's unique id (assigned by the database)
            name: the player's full name (as registered)
            wins: the number of matches the player has won
            matches: the number of matches the player has played
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM playerstandings;")

        return cursor.fetchall()


    def reportMatch(self, winner, loser):
        """Records the outcome of a single match between two players.

        Args:
          winner:  the id number of the player who won
          loser:  the id number of the player who lost
        """
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO matches VALUES (%s, %s);", (winner, loser))
        self.connection.commit()


    def swissPairings(self):
        """Returns a list of pairs of players for the next round of a match.

        Assuming that there are an even number of players registered, each player
        appears exactly once in the pairings.  Each player is paired with another
        player with an equal or nearly-equal win record, that is, a player adjacent
        to him or her in the standings.

        It wasn't made clear what should happen if there is a clear winner, so in
        that case I've decided to just return all of the players in their final
        order.

        Returns:
          A list of tuples, each of which contains (id1, name1, id2, name2)
            id1: the first player's unique id
            name1: the first player's name
            id2: the second player's unique id
            name2: the second player's name
        """
        standings = self.playerStandings()
        pairings = []
        # If there are at least 2 players...
        if len(standings) > 1:
            # If there is a winner...
            if standings[0][3] != standings[1][3]:
                # Return player standings
                pairings = [(standing[0], standing[1]) for standing in standings]
            else:
                # Pair each player with an adjacent player in the standings
                for i in range(0, len(standings), 2):
                    p1 = (standings[i][0], standings[i][1])
                    p2 = (standings[i+1][0], standings[i+1][1])
                    pairings.append((p1[0], p1[1], p2[0], p2[1]))
        return pairings



