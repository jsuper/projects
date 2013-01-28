package org.tony.dic.core.query.impl.test;

import org.junit.Test;
import org.tony.dic.core.query.Query;
import org.tony.dic.core.query.impl.NetQuery;

public class NetQueryTest {

	@Test
	public void testLookup() {
		System.setProperty("http.proxySet", "true");  
		System.setProperty("http.proxyHost", "10.32.235.41");  
		System.setProperty("http.proxyPort", "8080"); 
		
		Query query = new NetQuery();
		query.lookup("query");
	}
	
	@Test 
	public void testPrint(){
		System.out.println("中文");
		System.out.println("query".hashCode());
	}
}
