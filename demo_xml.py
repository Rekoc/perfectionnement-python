import xml.etree.ElementTree as ET
import random
import os, pathlib


root_file = pathlib.Path(__file__).parent.resolve()
path = os.path.join(root_file, "statics", "random.xml")
# Generate at https://onlinerandomtools.com/generate-random-xml
tree = ET.parse(path)
root = tree.getroot()
print(f"root tag --> {root.tag} // attributs --> {root.attrib}")

for tag in root:
    print(f"tag --> {tag.tag}")
    for total in tag.iter('total'):
        print(f"  total --> {total.text}")
        total.text = str(random.randint(1, 9999))
        new_val = "0" if int(total.get("u")) == "1" else "1"
        total.set("u", new_val)
        print(f"  NEW total --> {total.text}")

tree.write(path)

root = ET.Element('root')
tree = ET.ElementTree(root)
subroot = ET.SubElement(
    root, 'subroot',
    {"toto": "123"}
)
another_subroot = ET.SubElement(root, 'another_subroot')
subsubroot = ET.SubElement(
    subroot, 'subsubroot',
    {"tata": "12345"}
)
xml = ET.dump(root)
print(xml)

ET.indent(tree, space="\t", level=0)
with open('test.xml', 'wb') as f:
    tree.write(f)