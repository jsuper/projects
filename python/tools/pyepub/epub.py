import uuid
import zipfile

from datetime import datetime
from os.path  import exists, join as pjoin, relpath, splitext
from os       import walk
from file_op  import Dir, File
from template import *

class Epub():
    catlog_file = 'catlog.txt'
    def __init__(self,book_dir,title):
        self.title = title
        self.book_dir = book_dir
        self.output_dir = pjoin(book_dir,'target')
        self.ops_dir = pjoin(self.output_dir,'OPS')
        self.meta_inf_path = pjoin(self.output_dir, 'META-INF')
        self.container_dot_xml = pjoin(self.meta_inf_path, 'container.xml')
        self.mimetype_path = pjoin(self.output_dir,"mimetype")
        self.catlog_file = pjoin(book_dir, Epub.catlog_file)
    
    def init_resources(self):
        '''
        initial the necessary resources
        like:
            create target dir
            copy resources files to OPS dir
        '''
        self.uuid_urn = uuid.uuid4().urn
        self.date = datetime.now().strftime('%Y-%m-%d')
        self.toc_path = pjoin(self.ops_dir, 'toc.ncx')
        self.content_opf_path = pjoin(self.ops_dir, 'content.opf')
        
        Dir.remove_then_create(self.output_dir)
        Dir.create(self.meta_inf_path)
        Dir.copy(self.book_dir, self.ops_dir, 'target',Epub.catlog_file)
        

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
        if not exists(self.catlog_file):
            print 'Not found catlog file'
            return
        entries = [] #store catlog entry
        self.toc_entries = []
        with open(self.catlog_file) as f:
            lines = f.readlines()
            order = 0
            for line in lines:
                order = order + 1
                catlog = line.split(':')
                if len(catlog) == 2:
                    title = catlog[-1].strip().replace('&nbsp;',' ')
                    self.toc_entries.append(catlog[0].strip())
                    entries.append(
                        toc_nav_item_tpl.format(order,title, catlog[0].strip()))
        
        if len(entries) > 1:
            content = toc_format_tpl.format(self.uuid_urn, self.title, ''.join(entries))
            File.write(content, self.toc_path)
        
        
    def gen_content_opf(self):
        '''
        generate the content opf files
        '''
        file_list = []
        for root, dires, files in walk(self.ops_dir):
            for fname in files:
                fpath = relpath(pjoin(root,fname), self.ops_dir).replace('\\','/')
                f_id = self.file_id(fname)
                t_name, file_extension = splitext(fname)
                f_media_type = self.media_type_of(file_extension)
                file_list.append(opf_manifest_item_tpl.format(fpath,f_id, f_media_type))
        
        spine_toc = []
        if self.toc_entries and len(self.toc_entries)>0:
            for toc in self.toc_entries:
                idhref = toc.split('#')[0]
                spine_toc.append(opf_spine_toc_item_tpl.format(idhref))
    
        opf_content = opf_format_tpl.format(self.uuid_urn, self.date, 'tony', ''.join(file_list),
                                            ''.join(spine_toc))
        File.write(opf_content, self.content_opf_path)

    def gen_extra_files(self):
        '''
        generate the extra files of epub format
        e.g:
           mimetype
           META-INF
           container.xml
        '''
        File.write('application/epub+zip',self.mimetype_path)
        File.write(container_xml_tpl, self.container_dot_xml)

    def export(self):
        '''
        export to *.epub
        '''
        export_name = self.title+'.epub'
        epub = zipfile.ZipFile(pjoin(self.output_dir, export_name), 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in walk(self.output_dir):
            for fname in files:
                if not fname == export_name:
                    f_path = pjoin(root,fname)
                    epub.write(f_path,relpath(f_path,self.output_dir))
        epub.close()
        

    def media_type_of(self, file_suffix):
        '''
        return the file media-type
        '''
        if file_suffix == '.html' or file_suffix == '.htm' or file_suffix == '.xml':
            return 'application/xhtml+xml'
        elif file_suffix == '.ncx':
            return 'application/x-dtbncx+xml'
        elif file_suffix == '.png':
            return 'image/png'
        elif file_suffix == '.jpg':
            return 'image/jpeg'
        elif file_suffix == '.gif':
            return 'image/gif'
        elif file_suffix == '.css':
            return 'text/css'
        elif file_suffix == '.js':
            return 'text/javascript'
        else:
            return 'unknow'

    def file_id(self,file_name):
        if file_name.endswith('.ncx'):
            return 'ncx'
        else:
            return file_name


if '__main__' == __name__:
    sicp = Epub('C:/Users/tangilin/Desktop/EbookMaker/sicp_dl','sicp')
    sicp.generate()
