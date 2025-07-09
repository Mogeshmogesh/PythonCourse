# drone supply in mars
supplies=["oxygen tank","water","solar battery","thermal blanket","food pack"]
for item in supplies:
    print(item)
supplies.insert(0,"medical kit")
print(supplies)
supplies.remove("thermal blanket")
print(supplies)
supplies.insert(2,"navigation chip")
print(supplies)
delivary_item=supplies.pop()
print(supplies[:3])
supplies.reverse()
for item in supplies:
    print(item)
