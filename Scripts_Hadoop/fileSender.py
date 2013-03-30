"""
nitin2.kumar@one97.net
"""

import os
import sys
import paramiko
import pexpect

#server_list=("hadoopdata1","hadoopdata2","hadoopdata3","hadoopdata4","hadoopdata5","hadoopdata6","hadoopdata7","hadoopdata8","hadoopdata9","hadoopdata10","hadoopdata11","hadoopdata12","hadoopdata13","hadoopdata14")

server_list=("hadoopdata12",)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def scp_query(file,source_path):
    try:
        for server in server_list:
            query="scp %s hadoop@%s:%s/ "%(file,server,source_path)
            print query
            os.system(query)
    except Exception,e:
        print e

def execute_query(cmd):
    try:
        for server in server_list:
            ssh.connect(server, username='hadoop',password='548853ele')
            stdin, stdout, stderr=ssh.exec_command(cmd)
            data=stdout.readlines()
            for line in data:
                print line.strip('\n')
        ssh.close()

    except Exception,e:
        print e

def main():
    file=sys.argv[1]
    source_path=sys.argv[2]
    print file
    print source_path
    scp_query(file,source_path)
    newline="* 10 * * * java -jar %s/%s"%(source_path,file)
    cmd='(crontab -l; echo "%s") | crontab -'%(newline)
    print(cmd)
    execute_query(cmd)
    per="chmod 755 %s/%s"%(source_path,file)
    print(per)
    execute_query(per)

def run_query(query):
        foo=pexpect.spawn(query)
        foo.close()

if __name__ == "__main__":
    main()

