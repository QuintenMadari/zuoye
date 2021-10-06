#!/bin/env bash

########################################################
############## NOODZAKELIJKE CONFIGURATIE ##############

#REPOROOT="/absolute/path/to/my/repo-s/documentroot/"
#WEBDOCUMENTROOT="/path/to/var/www/html/webdocroot/"

REPOROOT="/home/qsr/code/zuoye/"
WEBDOCUMENTROOT="/var/www/html/zuoye/"


##-------------------## Trouwens ##-------------------##

# > zorg dat de documentroot de juiste rechten en groepen heeft
# > chown -R www-data:
# > check firewall (ufw) status van poorten
# > chmod 600 of 700 voor .ssh folder
# > enable site config met juiste docroot en juiste mods in apache/nginx
# > optioneel een link naar deployscript.sh op een handige plek (crontab)

########################################################
########################################################


#------------------------------------------------------#
#----------------|| Niet aankomen :) ||----------------#

# change directory naar repo root
cd $REPOROOT

# submodules initiele pull
git submodule update --init --recursive --remote
## > init eigk niet elke keer nodig, alleen 1e keer na clonen main repo
## > recursive pakt meteen elke submodule van de repo (.gitmodules)
## > remote zorgt voor het gaan naar de uiterste tip van de sub repo

# aanroepen script voor opzetten Docute
python3 ./deployment/makescript.py

# verplaatsen naar echte web documentroot
rm -rf $WEBDOCUMENTROOT
cp -r $REPOROOT $WEBDOCUMENTROOT

#------------------------------------------------------#
#------------------------------------------------------#