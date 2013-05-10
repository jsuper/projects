package org.tony.dic.core.query.impl;

import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.charset.Charset;

import org.tony.dic.core.query.Query;
import org.tony.opendict.core.Ctx;

public class NetQuery implements Query{
	
	private static final String QURL= "queryUrl" ;
	
	public void lookup(String word) {
		String queryUrl = Ctx.ctx().get(QURL);
		try {
			URL url = new URL(queryUrl+word);
			HttpURLConnection conn = (HttpURLConnection) url.openConnection() ;
			conn.connect() ;
			InputStream fis = conn.getInputStream() ;
			byte[] buff = new byte[128*1024];
			int len = 0 ;
			StringBuffer str = new StringBuffer();
			while((len=fis.read(buff))!=-1){
				str.append(new String(buff,0,len,Charset.forName("UTF-8")));
			}
			System.out.println(str);
			fis.close();
			conn.disconnect();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
