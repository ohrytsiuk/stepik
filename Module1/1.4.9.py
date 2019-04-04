n = int(input())

commands = []

for i in range(n):
    cmd, namespace, var = input().split()
    dictionary = {"cmd": cmd, "namespace": namespace, "var": var}
    commands.append(dictionary)


def search_namespace(namespace, var):
    if namespace is None:
        return None
    if variables.get(namespace) is not None:
        if var in variables.get(namespace):
            return namespace
        else:
            return search_namespace(namespaces.get(namespace), var)
    else:
        return search_namespace(namespaces.get(namespace), var)


namespaces = {}
namespaces['global'] = None
variables = {}

for i in commands:
    if i.get('cmd') == 'create':
        namespaces[i.get('namespace')] = i.get('var')
    if i.get('cmd') == 'add':
        # variables[i.get('namespace')] = {i.get('var'):i.get('var')}
        # variables[i.get('namespace')] = {}
        if variables.get(i.get('namespace')) is None:
            variables[i.get('namespace')] = {i.get('var'): i.get('var')}
        else:
            variables[i.get('namespace')][i.get('var')] = i.get('var')
        # vars.append(i.get('var'))
        # pass
    if i.get('cmd') == 'get':
        root = search_namespace(i.get('namespace'), i.get('var'))
        print(root)
