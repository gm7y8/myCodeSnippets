#def send_rest_data()

#adding table miss-flow entry

miss1={
    "dpid":1,
    "priority":22222,
    "match":{
        "dl_type":0x806
        "nw_proto":1        
        },
    "actions":"flood"
}



flow1={
    "dpid": 1,
    "priority": 22222,
    "match":{
        "in_port":2
         "dl_dst":"00:00:00:00:00:01"
    },
    "actions":[
        {
            "output": 1
        }
    ]
 }
 
 
flow2={
    "dpid": 1,
    "priority": 22222,
    "match":{
        "in_port":1
         "dl_dst":"00:00:00:00:00:02"
    },
    "actions":[
        {
            "output": 2
        }
    ]
 }
 
 

flow3={
    "dpid": 1,
    "priority": 22222,
    "match":{
        "in_port":1
         "dl_dst":"00:00:00:00:00:01"
    },
    "actions":[
        {
            "output": 2
        }
    ]
 }
 
 
flow4={
    "dpid": 1,
    "priority": 22222,
    "match":{
        "in_port":2
         "dl_dst":"00:00:00:00:00:02"
    },
    "actions":[
        {
            "output": 1
        }
    ]
 }
 
 
