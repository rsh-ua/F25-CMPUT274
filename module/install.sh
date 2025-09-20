#!/bin/bash

rcfile=""
cat ${SHELL} | egrep "bash" > /dev/null
bashFound=$?
if [ $bashFound -eq 0 ]; then 
  rcfile=".bashrc"
fi
cat ${SHELL} | egrep "zsh" > /dev/null
zshFound=$?
if [ $zshFound -eq 0 ]; then
  rcfile=".zshrc"
fi
nf=$((bashFound + zshFound))
if [ $nf -ge 2 ]; then
  echo "Shell unknown. Install script cannot complete task."
  echo "Are you using a course-approved method for running your programs? Either:"
  echo "wsl ubuntu install on windows"
  echo "terminal on mac"
  echo "Ask instructor for help on discussion forum."
  exit 1
fi

touch ~/${rcfile}

egrep -i "PYTHONPATH.*cmput274" ~/${rcfile} > /dev/null
if [ $? -eq 0 ]; then
  echo "Install script already executed, ask instructor for help if install not working"
  echo "To test if install is working follow the steps below exactly"
  echo "1. Open a NEW shell. Once installed anytime you open a shell it should work."
  echo "2. Run your python interpreter in the newly opened shell"
  echo "3. In your python interpreter try the following commands:"
  echo "        from cmput274 import *"
  echo "        empty()"
  echo "If your install is working then the above code will print out the value () in your Python interpeter"
  echo "If your install is not working then your Python interpreter will produce an error"
else
  echo "# Line added for CMPUT274 class" >> ~/${rcfile}
  s='export PYTHONPATH=${PYTHONPATH}:'"$(pwd)"
  echo ${s} >> ~/${rcfile}
fi
