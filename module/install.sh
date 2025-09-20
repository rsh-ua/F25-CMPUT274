#!/bin/bash

egrep "PYTHONPATH.*cmput274" ~/.bashrc > /dev/null
if [ $? -eq 0 ]; then
  echo "Install script already executed, ask instructor for help if install not working"
else
  echo "# Line added for CMPUT274 class" >> ~/.bashrc
  s='export PYTHONPATH=${PYTHONPATH}:'"$(pwd)"
  echo ${s} >> ~/.bashrc
fi
