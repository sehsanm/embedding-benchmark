

def write_result_to_file(data_set_name , totals , corrects,path):
    with open(path,"w") as f:
        f.write(":dataset "+data_set_name+"\n")
        for cat in totals:
            f.write(totals[cat]+","+corrects[cat]+"\n")