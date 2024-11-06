#!/usr/bin/python3
#### Kenneth Keopraseuth
#### inet_4031_adduser_script
#### Program Creation Date: 11/6/2024
#### Program Last Updated Date: 11/6/2024

import os #used to run system commands
import re #used for regular expression operations
import sys #used to read input from stdin

def main():
    for line in sys.stdin:

        # This regular expression checks if the line starts with '#' (indicating a comment)
        match = re.match("^#", line)

        # Splitting the line into fields using ':' as a delimiter
        fields = line.strip().split(':')

        # If the line is a comment or does not have exactly 5 fields, skip this line
        if match or len(fields) != 5:
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        #print cmd
        os.system(cmd)
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        #print cmd
        os.system(cmd)

        for group in groups:
            # Assign the user to the specified groups, unless the group field is '-'
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
