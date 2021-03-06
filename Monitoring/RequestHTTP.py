#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script check a list of websites
# and sends mail when the HTTP status code is not 200
#
# Used to check wheter all projects are up and running
# (not broken, say for example because a dependency library was removed)

# Author Ando Roots 2012
# Version 1.0
# Licence: Apache Licence Version 2.0
# http://sqroot.eu/2012/01/python-check-that-your-projects-are-still-alive/

import httplib
import yaml
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Holds the config options. Populated from the config file
config = None

# Buffers the output for e-mail
# Actual output is still shown in real time
output_buffer = ""

# Is set to False when any checked sites return HTTP code other than 200
# The report mail is sent when this is False
all_valid = True

# ------------- START config

DIR = ''

# Config filename
config_file = DIR + "http_check.yaml"

# This gets called when everything is OK
def http_ok(site):
    output(site['name'] + " reported OK.")
    return # Custom actions here

# This gets called when the status code is NOT 200
def http_error(site, http_status):
    output("<span style=\"color:#DD4B39;font-weight: bold;\">"+site['name'] + " FAILURE: HTTP status is "+ str(http_status)+".</span>")

    return # Any custom actions here

# -------------- END config - do not edit below unless you know what's going on

# Send script output to configured recipients (called on failure)
def send_report():
    global config, output_buffer

    # Create multipart message headers
    msg = MIMEMultipart('alternative')
    msg['Subject'] = config['mail']['subject']
    msg['From'] = config['mail']['sender']
    msg['To'] = config['mail']['recipients']

    if (not config['mail']['send_report']):
        return
    try:
        s = smtplib.SMTP('localhost')

        # Attach message body in plain and HTML
        part1 = MIMEText(output_buffer.replace("<br />", "\r\n"), 'plain')
        part2 = MIMEText(output_buffer, 'html')
        msg.attach(part1)
        msg.attach(part2)

        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()
        output('Sent script output to ' + msg['To'])
    except smtplib.SMTPException:
        output('Could not send error report to configured recipients!')

# Read a list of sites to check
def read_config():
    global config
    f = open(config_file)
    config = yaml.load(f)
    f.close()
    return config


# Function from http://stackoverflow.com/a/1140822/401554
# Get HTTP status code of a domain + path
def get_status_code(host, path="/", https = False):
    """ This function retreives the status code of a website by requesting
        HEAD data from the host. This means that it only requests the headers.
        If the host cannot be reached or something else goes wrong, it returns
        None instead.
    """
    try:
        if (https):
            conn = httplib.HTTPSConnection(host)
            print "HTTPS: "+host
        else:
            conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        return conn.getresponse().status
    except StandardError:
        return None


# Main - read config, check each site
def main():
    global all_valid, config

    output(str(datetime.now())+': Starting check.')

    # Contains a list of sites to check
    config = read_config()

    # Check each site
    for site in config['sites']:

        # Determine the path (in addition to the domain)
        if ('uri' in site):
            uri = "/"+site['uri']
        else:
            uri = '/'

        if ('https' in site):
            https = True
        else:
            https = False

        # Get the HTTP code
        code = get_status_code(site['domain'], uri, https)
        output("Checking "+site['name']+" ("+site['domain']+uri+") ... "+ str(code))

        # Call handler functions for status codes
        if (code == 200):
            http_ok(site)
        else:
            all_valid = False
            http_error(site, code)

    output(str(datetime.now())+': Checking completed.')

    # Send report when failures need reporting
    if (not all_valid):
        output('Some sites failed.')
        send_report()
    else:
        output('<span style="background-color: #79b530; font-weight: bold; font-size: 16px; color: #fff;">All sites reported status code 200.</span>')

    # Log results to a file
    if (config['file']['log']):

        try:
            # Status file
            f = open(config['file']['status_file'], 'w')
            f.write(str(all_valid))
            f.close()
        except Exception:
            output("Error writing status log file!")

        try:
            # Console output file
            f = open(config['file']['output_file'], 'w')
            f.write(output_buffer)
            f.close()
        except Exception:
            output('Error writing output buffer file')

# Buffer output for e-mail
def output(string):
    global output_buffer
    output_buffer += "<br />"+string
    print string


# Call the main function
main()