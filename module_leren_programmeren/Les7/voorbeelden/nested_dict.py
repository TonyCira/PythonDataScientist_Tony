myFamily= []

myFamily["child1"] = {"name":"kyra", "year": 2008}
myFamily["child2"] = {"name":"lisa", "year": 2010}
myFamily["child3"] = {"name":"emma", "year": 2010}

for k_family, v_family in myFamily.items():
    print(k_family)
    for k_child, v_child in v_family.items():
        print(f"   {k_child}: {v_child}")
