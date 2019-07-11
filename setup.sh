# This setup is just to automate the copying & deleting stuff. 

YELLOW="\033[33m"
BLUE='\033[1;34m'

chmod 777 search4.py
echo -e $YELLOW setting up search4.
sleep 0
cp search4.py $HOME/search4
# Removing the extra file
rm -rf search4.py
cd
sleep 0
echo -e $BLUE Setup done. use search4 , on the terminal.
