import os
import re

r = re.compile("([0-9]{2,3})_(.*).xml")
for filename in os.listdir("arena_defs"):
    m = r.search(filename)
    num = m.group(1)
    name = m.group(2)
    os.rename("arena_defs/" + filename, "arena_defs/" + name + '_' + num + ".xml")
