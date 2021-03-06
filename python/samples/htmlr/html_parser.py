#coding=utf-8
import sys

class Node:
    "Define each node for sgml tag"
    
    def __init__(self, name):
        self.name = name 
        self.text = None
        self.children = []
        self.tag_closed = None
        self.attributes = dict()
        self.is_self_closed_tag = False

    def append_child(self, node):
        "Append an node in children"
        self.children.append(node)
    
    def set_text(self, text):
        self.text = text

    def add_attribute(self, key, value):
        self.attributes[key] = value

class Token:
    def __init__(self, start, value, end=-1, line = -1):
        self.start = start 
        self.value = []
        self.value.append(value)
        self.end = end
        self.line = line
        self.pure_value = None

    def append(self, char):
        self.value.append(char)

    def get_value(self):
        if not self.pure_value:
            self.pure_value = ''.join(self.value)            

        return self.pure_value

    def __str__(self):
        return self.get_value()


def html_parser(html_file_path):
    tokens = []
    html_file = open(html_file_path,'r')
    try:
        token = None
        line_count = 0
        char_count = 0
        first_quote_char = False
        next_space_is_text = False
        all_next_char_should_continue = False
        while True:
            lines = html_file.readlines(1024)
            if not lines:
                break
            for line in lines:
                line_count += 1
                for char in line:
                    char_count += 1
                    if all_next_char_should_continue and (not (char == '"')) and token:
                        token.append(char)
                        continue
                    if char == '<':
                        if token:
                            tokens.append(token)
                        tokens.append(Token(char_count,char,char_count+1,line_count))
                        token = None
                        next_space_is_text = False
                    elif char == '>':
                        if token:
                            tokens.append(token)
                        token = None
                        tokens.append(Token(char_count,char,char_count+1,line_count))
                        next_space_is_text = True
                    elif char == ' ':
                        if token and next_space_is_text:
                            token.append(char)
                            continue

                        if token and first_quote_char:
                            token.append(char)
                        elif token and not first_quote_char:
                            token.end = char_count
                            tokens.append(token)
                            token = None
                    elif char == '"':
                        if not first_quote_char:
                            if token:
                                tokens.append(token)
                                token = None
                            token = Token(char_count,char,-1,line_count)
                            first_quote_char = True
                            all_next_char_should_continue = True
                        else:
                            all_next_char_should_continue = False
                            first_quote_char = False
                            token.append(char)
                            token.end = char_count
                            tokens.append(token)
                            token = None
                    elif char=='\n':
                        continue
                    else:
                        if not token:
                            token = Token(char_count, char, -1, line_count)
                        else:
                            token.append(char)
    except:
        import traceback
        print traceback.format_exc(sys.exc_info()[0])
    finally:
        html_file.close()
    
    return tokens;

def parse_tags(tokens):
    '''
    parse tokens to html tag
    '''
    html_tags = []
    html_node = None
    html_node_attribute_start = False
    html_tag_name = None
    while len(tokens) > 0 :
        current = tokens.pop(0)
        if current == '<':
            next_tag_name = tokens.pop(0).get_value()
            if not html_node:
                html_tag_name = []
                html_tag_name.append(next_tag_name)
                html_node_attribute_start = True
            else:
                if next_tag_name.startswith('/') and next_tag_name[1:] == html_node.name:
                    #handling the tag close
                    html_node.tag_closed = True
                    pre_node = html_tags.pop()
                    if not pre_node.tag_closed:
                        pre_node.append(html_node)
                        html_tags.append(pre_node)
                    else:
                        html_tags.append(pre_node)
                        html_tags.append(html_node)
                    html_node = None
        elif current == '/':
            #handling self closed tag
            next_tag_name = tokens.pop(0).get_value()
            if next_tag_name == '>' and html_node:
                html_node.is_self_closed_tag = True
                html_node.tag_closed = True
                pre_node = html_tags.pop()
                if not pre_node.tag_closed:
                    pre_node.append(html_node)
                    html_tags.append(pre_node)
                else:
                    html_tags.append(pre_node)
                    html_tags.append(html_node)
                html_node = None
                    
            
        
if '__main__'  == __name__:
    tokens = html_parser('html.html')
    for t in tokens:
        print t
