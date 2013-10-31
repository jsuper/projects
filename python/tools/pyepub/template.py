#define the epub file template

opf_format_tpl = '''<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="2.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
    <dc:identifier id="BookId" opf:scheme="UUID">{0}</dc:identifier>
    <dc:date opf:event="modification">{1}</dc:date>
    <meta content="0.7.3" name="{2}" />
  </metadata>
  <manifest>
    {3}
  </manifest>
  <spine toc="ncx">
    {4}
  </spine>
  <guide />
</package>
'''

opf_manifest_item_tpl = '''<item href="{0}" id="{1}" media-type="{2}" />\n'''
opf_spine_toc_item_tpl = '''<itemref idref="{0}" />\n'''

toc_format_tpl='''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN"
 "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="{0}" />
    <meta name="dtb:depth" content="1" />
    <meta name="dtb:totalPageCount" content="0" />
    <meta name="dtb:maxPageNumber" content="0" />
  </head>
  <docTitle>
    <text>{1}</text>
  </docTitle>
  <navMap>
     {2}
  <navMap>
</ncx>
'''

toc_nav_item_tpl='''    <navPoint id="navPoint-{0}" playOrder="{0}">
      <navLabel>
        <text>{1}</text>
      </navLabel>
      <content src="{2}" />
    </navPoint>
'''

container_xml_tpl = '''<?xml version="1.0" encoding="UTF-8" ?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
   <rootfiles>
      <rootfile full-path="OPS/content.opf" media-type="application/oebps-package+xml"/>
   </rootfiles>
</container>
'''
