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
#print node1,node2
g={}
for el in l[0:length-2]:
	#print el
	kv=el.split("->")
	#print kv[0],kv[1]
	g[kv[1]]=kv[0]
#print str(g)

x=find_manager(g,node1,[]);

y=find_manager(g,node2,[]);

#print x,y
for i in x:
	if i in y:
		print i
		break
