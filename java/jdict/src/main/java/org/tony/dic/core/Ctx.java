package org.tony.dic.core;

import java.io.InputStream;
import java.util.Iterator;
import java.util.Properties;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;

public final class Ctx {

	private static final String defaultConfig = "/config/config.properties" ;
	private static Ctx ctx ;
	private ConcurrentMap<String, String> map ;

	public static final Ctx ctx() {
		if (ctx == null) {
			synchronized (Ctx.class) {
				if (ctx == null) {
					ctx = new Ctx();
				}
			}
		}
		return ctx;
	}
	
	private Ctx(){
		map = new ConcurrentHashMap<String, String>();
		InputStream fis= Ctx.class.getResourceAsStream(defaultConfig);
		try{
			if(fis!=null) {
				Properties pro = new Properties() ;
				pro.load(fis);
				Iterator<Object> keyIter = pro.keySet().iterator() ;
				while(keyIter.hasNext()) {
					String key = (String)keyIter.next() ;
					String value = pro.getProperty(key);
					map.put(key, value);
				}
			}
		}catch (Exception e) {
			System.out.println(e);
		}
	}
	
	public String get(String key) {
		return this.map.get(key);
	}
}
