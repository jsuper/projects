import uuid

from datetime import datetime
from os.path  import exists, join as pjoin 
from file_op  import Dir

class Epub():
    catlog_file = 'catlog.txt'
    def __init__(self,book_dir,title):
        self.book_dir = book_dir
        self.output_dir = pjoin(book_dir,'target')
        self.ops_dir = pjoin(self.output_dir,'OPS')
        self.catlog_file = pjoin()
    
    def init_resources(self):
        '''
        initial the necessary resources
        like:
            create target dir
            copy resources files to OPS dir
        '''
        self.uuid_urn = uuid.uuid4().urn
        self.date = datetime.now().strftime('%Y-%m-%d')
        Dir.remove_then_create(self.output_dir)
        Dir.copy(book_dir, self.ops_dir, ['target',Epub.catlog_file])
        

    def generate(self):
        '''
        start generate epub
        '''
        self.init_resources()
        self.gen_toc()
        self.gen_content_opf()
        self.gen_extra_files()
        self.export()
    
    def gen_toc(self):
        '''
        generate the toc.ncx files
        '''
        
        
    def gen_content_opf(self):
        '''
        generate the content opf files
        '''

    def gen_extra_files(self):
        '''
        generate the extra files of epub format
        e.g:
           mimetype
           META-INF
           container.xml
        '''

    def export(self):
        '''
        export to *.epub
        '''
