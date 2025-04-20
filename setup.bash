#!/bin/bash

if [[ ! -d .venv ]]
then
   echo "Setting up Virtual Environment"
   virtualenv .venv  && source .venv/bin/activate && pip3 install -r requirements.txt
else
   source .venv/bin/activate
fi
