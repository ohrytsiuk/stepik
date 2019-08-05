import xml.etree.ElementTree as ElementTree


def get_children(root, level=0):
    level += 1
    for key, value in root.attrib.items():
        dc[value] += level
    data = root.findall(root.tag)
    for i in data:
        get_children(i, level)


dc = {'red': 0,
      'green': 0,
      'blue': 0}

tree = ElementTree.parse('cube.xml')
# tree = ElementTree.fromstring(input())

root = tree.getroot()

get_children(root)

print(str(dc.get('red')) + ' ' + str(dc.get('green')) + ' ' + str(dc.get('blue')))



