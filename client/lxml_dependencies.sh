#!/bin/bash


function install_lxml_dependencies () 
{
    echo "----------------------------------------------";
    sudo apt-get install libxml2 libxslt1.1 libxslt-dev;
    echo "----------------------------------------------";
}

if [ $USER = "root"]
then
    install_lxml_dependencies;
else

    echo "To install lxml dependencies you should be root user. If you have this depencies installed, skip this step pressing n";
    echo "Do you want install it? [y/n]";
    read option;
    case $option in
        y) install_lxml_dependencies;;
        n) echo "--------------------------------------------";;
    esac;
fi

