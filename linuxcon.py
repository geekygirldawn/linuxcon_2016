#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Copyright (C) 2015 Dawn M. Foster
# Licensed under GNU General Public License (GPL), version 3 or later: http://www.gnu.org/licenses/gpl.txt

# LinuxCon 2015 Presentations
# Network analysis: People and open source communities

import fileinput        # used for file operations
import os		# used to merge dir and filename
import sys, getopt      # used to read options 
import MySQLdb		# for mysql

def usage():
    print ""
    print "linuxcon.py"
    print "Copyright (C) 2015 Dawn M. Foster"
    print "Licensed under GNU General Public License (GPL), version 3 or later:"
    print "http://www.gnu.org/licenses/gpl.txt"
    print ""
    print "Assumes you are using a MySQL database on localhost and that you have a my.cnf file."
    print "The month and year are hardcoded into the query for this example to make data manageable,"
    print "but you can remove that part of the query if you want to use it for all data."
    print """
-h, --help
-o, --outputfiledir   OUTFILEDIR: Set the directory for the output files where
                      you want to store them. If these files exist, the 
                      originals will OVERWRITTEN.
-d, --database	      DATABASE: the database name to query.
"""

def main(argv):
    output_file_dir=''

    try: 
        opts, args = getopt.getopt(argv, "ho:d:", ["help","outputfiledir=","database="])
    except getopt.GetoptError:
        print 'Usage: linuxcon.py -o <outputfiledir> -d <database>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif opt in ("-o", "--outputfiledir"):
            output_file_dir = arg
        elif opt in ("-d", "--database"):
            database = arg

    # Prepare output file

    output_file_gource  = os.path.join(output_file_dir, 'mailing_list_custom_log.csv')
    gource = open(output_file_gource, 'w')

    # Output messages to make sure user has the correct details

    print 'Writing output files as:'
    print 'Gource: ', output_file_gource
    print 'Database:', database

    # Prepare database

    db = MySQLdb.connect(db=database, read_default_file="~/.my.cnf");
    cursor = db.cursor()

    # Run query
    try: 
        cursor.execute("SELECT unix_timestamp(DATE_ADD(m.first_date, interval m.first_date_tz second)) AS unix_date, mp.email_address AS sender, (SELECT mp2.email_address FROM messages m2, messages_people mp2 WHERE m2.is_response_of=m.is_response_of AND mp2.message_id=m2.is_response_of limit 1) AS receiver FROM messages_people mp, messages m WHERE YEAR(m.first_date)=2015 AND MONTH(m.first_date)=1 AND mp.message_id=m.message_id;")
    except:
        print 'Error: Unable to retreive data'

    posts = cursor.fetchall()

    for row in posts:
            unix_date = row[0]
            email = row[1]
            response_of_email = row [2]
            username = email.split("@")[0]
            if response_of_email is None: # new threads
                gource.write("%s|%s|A|new\n" % (unix_date, username))
            elif email == response_of_email: # self-replies
                pass
            else:
                username_response_of = response_of_email.split("@")[0]
                gource.write("%s|%s|M|%s\n" % (unix_date, username, username_response_of))

    # disconnect from database and close files
    db.close()
    gource.close()

    # Sort Gource file by timestamp
    try:
        gource = open(output_file_gource, 'r')
        try: 
            lines = gource.readlines()
            lines.sort()
            gource.close()
            gource = open(output_file_gource, 'w')
            gource.writelines(lines)
        finally:
            gource.close()
    except:
        print 'Cannot open Gource file for sorting'

if __name__ == "__main__":
   main(sys.argv[1:])


