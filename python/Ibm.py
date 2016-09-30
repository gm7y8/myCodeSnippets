def find_relationship(g,node1,node2):
	if g.has_key(node1) and g.has_key(node2):
		if g.get(node1) == g.get(node2):
			print "found manager"
			print g.get(node1)
		else:
			find_relationship(g,g.get(node1),g.get(node2))


def find_manager(g,node,path):
	path=path+[node]
	if g.has_key(node):
		new_path=find_manager(g,g.get(node),path)
		if new_path: return new_path
	return path



var=raw_input()
l=var.split(",")
length=len(l)
node1=l[length-2]
node2=l[length-1]
print node1,node2
g={}
for el in l[0:length-2]:
	print el
	kv=el.split("->")
	print kv[0],kv[1]
	#if g.has_key(kv[1]):
	#	g[kv[1]].append(str(kv[0]))
	#else:
		#g[kv[1]]=[kv[0]]
	g[kv[1]]=kv[0]
print str(g)
#print find_relationship(g,node1,node2)

#print g.get(node1) == g.get(node2)

print find_manager(g,'E',[])

print find_manager(g,'F',[])

man=list(set(find_manager(g,'E',[])) & set(find_manager(g,'F',[])));

print man


