#def send_rest_data()



flow1={
    "dpid": 1,
    "priority": 22222,
    "match":{
        "in_port":1
         "dl_dst":"00:00:00:00:00:01"
    },
    "actions":[
        {
            "output": 1
        }
    ]
 }
 
 
