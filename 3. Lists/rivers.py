rivers = ['danube', 'thames', 'seine', 'volga','ural', 'dnieper', 'don']
print(rivers[0])

rivers.append('vistula')
print(rivers)

del rivers[3]
print(rivers)

popped_rivers = rivers.pop()
print(rivers)
print(popped_rivers)

rivers.remove('ural')
print(rivers)

rivers.sort(reverse=True)
print(rivers)