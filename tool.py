import sys, os, base64
from urllib.parse import unquote
from urllib.parse import quote

usage = '''\nUsage: this.py [obf|deobf] [filename.html]\n\nNOTE: Files deobfuscated with this tool MUST have been obfuscated with it as well.'''

if len(sys.argv)!=3:
    print(usage)
    sys.exit(0)
opr=sys.argv[1]
file=sys.argv[2]
if not os.path.isfile(file):
    print ('''\nFile not found!''')
    sys.exit(0)
    
begst = '''<!DOCTYPE html>
<script type="text/javascript">
document.write(decodeURIComponent(atob(\''''

endst = '''\')));
</script>
<noscript>You must enable javascript in your browser to view this webpage.</noscript>
'''


if opr == "obf":
    data = open(file, 'r').read()
    data = quote(data)
    data = data.encode("utf-8")
    data = base64.b64encode(data)
    data = data.decode("utf-8")
    data = begst + data + endst
    out = open(file, 'w').write(data)
    print("\nSuccesfully Obfuscated %s" % file)
elif opr == "deobf":
    data = open(file, 'r').read()
    data = data[88:-102]
    data = data.encode("utf-8")
    data = base64.b64decode(data)
    data = data.decode("utf-8")
    data = unquote(data)
    out = open(file, 'w').write(data)
    print("\nSuccesfully Deobfuscated %s" % file)
else:
    print(usage)
    sys.exit(0)
