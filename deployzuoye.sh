#!/bin/env bash

## remarks
# .ssh chmod 700 or 600
# ufw
# chown -R www-data:

cd ~/code/zuoye
#primary pull in van submodules
git submodule update --init --recursive --remote
#init niet nodig voor tweede keer, maar remote zorgt voor het gaan naar de uiterste tip van de sub repo
python3 ./makescript.py
rm -rf /var/www/html/zuoye
cp -r ~/code/zuoye /var/www/html/
