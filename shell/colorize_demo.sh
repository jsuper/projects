#!/bin/bash

#define color 
RED=$(tput setaf 1)          #red
GRN=$(tput setaf 2)          #green
CYAN=$(tput setaf 6)         #cyan

#define font style
BOLD=$(tput bold)            #set font-weight to bold
RESET=$(tput sgr0)           #reset all terminal info configuration


colorize() {
    echo -e $@${RESET}
}

colorize_bold() {
    echo -e ${BOLD}$@${RESET}
}

colorize $RED HELLO
colorize_bold $CYAN This is bold
colorize_bold $GRN This is green bold
echo -e Hello\r
