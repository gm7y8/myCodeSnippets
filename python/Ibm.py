def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

var=raw_input()
l=var.split(",")
length=len(l)
node1=l[length-1]
node2=l[length-2]
print node1,node2
g={}
for el in l[0:length-2]:
	print el
	kv=el.split("->")
	print kv[0],kv[1]
	if g.has_key(kv[0]):
		g[kv[0]].append(""+kv[1]+"")
	else:
		g[kv[0]]=[kv[1]]
for i in g:
    print i, g[i]

print find_path(g,node2,node1)
