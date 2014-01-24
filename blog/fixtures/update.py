import os, sys

FIXTURE_DIR = os.path.dirname(__file__)
FIXTURE = os.path.join(FIXTURE_DIR, "blog.json")
MANAGE_PY = os.path.normpath(os.path.join(FIXTURE_DIR, "../../manage.py"))

def execute_management_command(args):
    cmd = "python " + MANAGE_PY + " " + args
    print cmd
    rc = os.system(cmd)
    if rc == 0:
        print "ok"
    else:
        print "FAILED"

def usage():
    print "python update.py dump"
    print "python update.py load"
    sys.exit(1)

def main():
    if len(sys.argv) != 2:
        usage()
    arg = sys.argv[1]
    if arg == "dump":
        execute_management_command("dumpdata --indent 2 blog > " + FIXTURE)
    elif arg == "load":
        execute_management_command("syncdb ")
        execute_management_command("loaddata " + FIXTURE)
    else:
        usage()

if __name__ == "__main__":
    main()

