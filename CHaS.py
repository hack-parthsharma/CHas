#!/usr/bin/python
# Originally by NaN - http://swin.es/g/NaN/CHaS/blob/master/CHaS.pl
# Rewritten by Parth from perl to python
#

from __future__ import print_function
import subprocess
import threading
import argparse
import os
import sys
import time

class CHaS:

    target = ""
    report_location = ""
    arguments = []

    def __init__(self, arguments):

        self.arguments = arguments

#        if self.arguments.target == "" and self.arguments.install == True:
#            self.install_requirements()
#            exit()

        self.arguments.target = arguments.target
        self.tool_location = os.path.dirname(os.path.realpath(__file__))
        if self.arguments.out is not None:
            self.report_location = self.arguments.out
        else:
            self.report_location = "Reports/{0}".format(self.arguments.target.replace("://", "__"))

        if False == os.path.exists(self.report_location):
            os.makedirs(self.report_location, 0o775)
        else:
            self.report_location = self.report_location + \
                "_" + str(int(time.time()))
            os.makedirs(self.report_location)

    def install_requirements(self):
        print("[+] Launching Installer Script...")
        s = subprocess.call(["{0}/setup.sh".format(os.path.dirname(os.path.abspath(__file__)))])
        return s

    def do_sslscan(self):
        print("[+] Starting SSLScan")
        proc = subprocess.Popen("{2}/Tools/sslscan/sslscan {0} > {1}/sslscan.html".format(
            self.arguments.target, self.report_location, self.tool_location), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
        proc.communicate()
        print("[+] Finished SSLScan")
        return True

    def do_testssl(self):
        print("[+] Starting TestSSL (This may take a while)")
        proc = subprocess.Popen("{2}/Tools/testssl.sh/testssl.sh {0} > {1}/testssl.html".format(
            self.arguments.target, self.report_location, self.tool_location), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
        proc.communicate()
        print("[+] Finished TestSSL")
        return True

    def do_check_headers(self):
        print("[+] Starting CheckHeaders")
        proc = subprocess.Popen("python {2}/Tools/securityheaders/securityheaders.py --max-redirects 5 {0} > {1}/headers.html".format(
            self.arguments.target, self.report_location, self.tool_location), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
        proc.communicate()
        print("[+] Finished CheckHeaders")
        return True

    def do_nmap_scan(self):
        print("[+] Starting Nmap scan")
        proc = subprocess.Popen("nmap -p- -A -vvv --min-rate 1200 --max-retries 2 -sT -oA {1}/tcp_connect.full {0}".format(
            self.arguments.target, self.report_location, self.tool_location), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
        proc.communicate()
        print("[+] Finished Nmap scan")
        return True

    def do_nikto_scan(self):
        print("[+] Starting Nikto scan")
        proc = subprocess.Popen("{2}/Tools/nikto/program/nikto.pl -nointeractive -output {1} -host {0} >/dev/null".format(
            self.arguments.target, self.report_location, self.tool_location), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
        proc.communicate()
        print("[+] Finished Nikto scan")
        return True

    def do_dirsearch(self):
        print("[+] Starting DirSearch scan")
        proc = subprocess.Popen("{2}/Tools/dirsearch/dirsearch.py -u '{0}' -e php,jsp,aspx,md,txt,zip -t40 --random-agents  -r -f -w {2}/Tools/SecLists/Discovery/Web-Content/raft-large-files.txt > {1}/dirsearch.txt".format(
            self.arguments.target, self.report_location, self.tool_location), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
        proc.communicate()
        print("[+] Finished DirSearch scan")
        return True

    def do_wig_scan(self):
        print("[+] Starting Wig scan")
        proc = subprocess.Popen("python3 {2}/Tools/wig/wig.py -q {0}  > {1}/wig.html".format(
            self.arguments.target, self.report_location, self.tool_location), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
        proc.communicate()
        print("[+] Finished Wig scan")
        return True

    def do_davtest_scan(self):
        print("[+] Starting DavTest scan")
        proc = subprocess.Popen("{2}/Tools/davtest/davtest.pl -cleanup -quiet -url {0} > {1}/davtest.html".format(
            self.arguments.target, self.report_location, self.tool_location), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
        proc.communicate()
        print("[+] Finished DavTest scan")
        return True

    def do_wafw00f_scan(self):
        print("[+] Starting wafw00f scan")
        proc = subprocess.Popen("{2}/Tools/wafw00f/wafw00f -cleanup -quiet -url {0}  > {1}/wafw00f.html".format(
            self.arguments.target, self.report_location, self.tool_location), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
        proc.communicate()
        # print("[!] wafw00f is currently unsupported")
        return True

    def do_whatweb_scan(self):
        print("[+] Starting WhatWeb scan")
        proc = subprocess.Popen("{2}/Tools/WhatWeb/whatweb --no-errors -a 3 --colour=always {0} > {1}/WhatWeb.html".format(
            self.arguments.target, self.report_location, self.tool_location), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
        proc.communicate()
        print("[+] Finished WhatWeb scan")
        return True

    def do_metagoo_scan(self):
        print("[+] Starting MetaGoo scan")
        proc = subprocess.Popen("python {2}/Tools/metagoofil/metagoofil.py -d {0} -t pdf,doc,xls,ppt,docx,xlsx,pptx -l100 -h yes {1}/downloaded_docs -f {1}/metagoofil.html".format(
            self.arguments.target, self.report_location, self.tool_location), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
        proc.communicate()
        print("[+] Finished MetaGoo scan")
        return True

    def launch_scans(self):
        print("[+] Reports are stored here: {0}".format(self.report_location))
        threads = []
        if "a" in self.arguments.scans or "c" in self.arguments.scans:
            threads.append(threading.Thread(target=self.do_check_headers))

        if "a" in self.arguments.scans or "s" in self.arguments.scans:
            threads.append(threading.Thread(target=self.do_sslscan))

        if "a" in self.arguments.scans or "t" in self.arguments.scans:
            threads.append(threading.Thread(target=self.do_testssl))

        if "a" in self.arguments.scans or "n" in self.arguments.scans:
            threads.append(threading.Thread(target=self.do_nmap_scan))

        if "a" in self.arguments.scans or "k" in self.arguments.scans:
            threads.append(threading.Thread(target=self.do_nikto_scan))

        if "a" in self.arguments.scans or "d" in self.arguments.scans:
            threads.append(threading.Thread(target=self.do_dirsearch))

        if "a" in self.arguments.scans or "w" in self.arguments.scans:
            threads.append(threading.Thread(target=self.do_wig_scan))

        if "a" in self.arguments.scans or "v" in self.arguments.scans:
            threads.append(threading.Thread(target=self.do_davtest_scan))

        if "a" in self.arguments.scans or "f" in self.arguments.scans:
            threads.append(threading.Thread(target=self.do_wafw00f_scan))

        if "a" in self.arguments.scans or "W" in self.arguments.scans:
            threads.append(threading.Thread(target=self.do_whatweb_scan))

        if "a" in self.arguments.scans or "m" in self.arguments.scans:
            threads.append(threading.Thread(target=self.do_metagoo_scan))

        print("[+] Running with {0} Threads".format(len(threads)))
        for t in threads:
            t.start()
            # t.join()

def main():
    parser = argparse.ArgumentParser(description="Check Headers and SSL (CHaS) - Written by NaN & Mantis")
    parser.add_argument("--install", action="store_true", help="Run the installer script")
    parser.add_argument("-t", "--target", default="", help="The target host to scan")
    parser.add_argument("-b", "--browser", required=False, help="The file browser to use to open the results (optional). Nautilus, thunar, etc")
    parser.add_argument("--scans", required=False, nargs="+", default="a", help="Types of scans to launch:\na - All\nc - Check Headers\ns - SSLScan\nt - TestSSL")
    parser.add_argument("-v", "--verbose", required=False, action="store_false", help="Types of scans to launch:\na - All\nc - Check Headers\ns - SSLScan\nt - TestSSL")
    parser.add_argument("-o", "--out", required=False, help="Custom output directory")
    arguments = parser.parse_args()


    chas = CHaS(arguments)
    if arguments.target == "" and arguments.install == True:
        chas.install_requirements()
        exit()

    #if arguments.target[0:7] != "http://" and arguments.target[0:8] != "https://":
    #    print("Please specify a URL. This only works on web-technologies.")
    #    exit()
    chas.launch_scans()

    # if arguments.browser is not None:
    #     subprocess.call("{0} {1}".format(arguments.browser, chas.report_location))

if __name__ == '__main__':
    main()
