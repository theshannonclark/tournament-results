# Project: Tournament Results - Shannon Clark

This is a project developed as part of Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004). The aim of this project is to develop a Python module that tracks a [Swiss-system tournament](https://en.wikipedia.org/wiki/Swiss-system_tournament) using a PostgreSQL database.

## Getting Started
This project is designed to run inside of a virtual machine. To do that, you'll need to install VirtualBox, and Vagrant, before cloning this repository, and running the VM.

### Installing VirtualBox
VirtualBox is the software that actually runs the VM. You can download the version of VirtualBox you need for your operating system from [here](https://www.virtualbox.org/wiki/Downloads). You won't need to run VirtualBox directly.

### Installing Vagrant
Vagrant is a piece of software used to provision, and configure a virtual machine. You can download the version of Vagrant you need for your operating system from [vagrantup.com](https://www.vagrantup.com/downloads.html).

## Install Tournament Results
You can download this project by cloning the git repository:

```
git clone https://github.com/theshannonclark/tournament-results.git
```

Then you can change into the resulting directory:

```
cd tournament-results
```

and run the virtual machine:

```
vagrant up
```

This will provision the virtual machine with the settings from Vagrantfile, and preinstall all of the other required software by running pg_config.sh.

After that is finished, connect to the virtual machine using ssh:

```
vagrant ssh
```

From here, you can find the project files by entering:

```
cd /vagrant/tournament
```

## Set up the tournament database
All of the SQL commands needed to set up the database are defined in /vagrant/tournament/tournament.sql. All you need to do is connect to the PostgreSQL interactive terminal:

```
psql
```

and import the SQL file:

```
\i tournament.sql
```

## Run the tests

If you're still in the psql prompt, quit with this command:

```
\q
```

Then run the tournament_test.py file:

```
python tournament_test.py
```
