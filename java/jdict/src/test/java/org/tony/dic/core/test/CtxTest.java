package org.tony.dic.core.test;

import org.junit.Assert;
import org.junit.Test;
import org.tony.dic.core.Ctx;

public class CtxTest {
	
	@Test
	public void testGet() {
		String key = "queryUrl" ;
		String data = Ctx.ctx().get(key);
		Assert.assertNotNull(data);
		System.out.println(data);
	}
}
