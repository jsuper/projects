
def print_header(header_str):
    print ''
    h_str = '\t|   ' + header_str + '   |'
    h_len = len(h_str)
    for i in range(1,3):
        if i==1:
            line = '\t '+ '-'*(h_len-3) + ' '
        else:
            line = '\t|'+' '*(h_len-3)+'|'
        
        print line

    print h_str
    for i in range(1,3):
        if i == 2:
            line = '\t '+'-'*(h_len-3)+' '
        else:
            line = '\t|' + ' '*(h_len-3)+'|'
        
        print line

    print ''


def print_to_table(_dict,terminal_with=60):
    """
    print given dict to terminal like a table
    """
    max_len = 1 
    keys = _dict.keys()
    keys_length = len(keys)
    for key in keys:
        fmt_str = str(key)+': '+str(_dict[key])
        max_len = max(len(fmt_str),max_len)
    
    max_len += 2
    number_cols = int(terminal_with/max_len)
    i = 0
    for key in keys:
        print '{0}: {1:{2}}'.format(key,_dict[key],max_len),
        i = i+1
        if i % number_cols == 0:
            print '\n',


