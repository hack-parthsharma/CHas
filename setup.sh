#!/bin/bash
top=`pwd`
mkdir -p Tools

# Install dependencies
sudo apt install nmap perl python python3 build-essential -y
sudo cpan install http::dav
sudo cpan install Getopt::Long

# Install tools
# Todo: Add EyeWitness
echo -e "Installing aha\n" && git clone https://github.com/masukomi/aha.git Tools/aha && cd Tools/aha && make && cd $top
echo -e "Installing sslscan\n" && git clone https://github.com/rbsec/sslscan.git Tools/sslscan && cd Tools/sslscan && sudo apt-get install build-essential git zlib1g-dev -y && make static && cd $top
echo -e "Installing TestSSL\n" && git clone --depth 1 https://github.com/drwetter/testssl.sh.git Tools/testssl.sh
echo -e "Installing SecurityHeaders\n" && git clone https://github.com/juerkkil/securityheaders.git Tools/securityheaders
echo -e "Installing Nikto\n" && git clone https://github.com/sullo/nikto.git Tools/nikto
echo -e "Installing DirSearch\n" && git clone https://github.com/maurosoria/dirsearch.git Tools/dirsearch 
echo -e "Grabbing SecLists\n" && git clone https://github.com/danielmiessler/SecLists.git Tools/SecLists
echo -e "Installing wig\n" && git clone https://github.com/jekyc/wig Tools/wig
echo -e "Installing DavTest\n" && git clone https://github.com/cldrn/davtest.git Tools/davtest
echo -e "Installing wafw00f\n" && pip install --user wafw00f
echo -e "Installing WhatWeb\n" && git clone https://github.com/urbanadventurer/WhatWeb.git Tools/WhatWeb
echo -e "Installing Metagoofil\n" && git clone https://github.com/kurobeats/metagoofil.git Tools/metagoofil
echo -e "Installing WAScan\n" && git clone https://github.com/m4ll0k/WAScan.git Tools/WAScan && pip install --user -r Tools/WAScan/requirements.txt && cd $top
mkdir -p Reports
echo "#############################################################"
echo -e "\n\n"
echo "All setup and ready to go!"
echo -e "\n\n"
echo "#############################################################"
