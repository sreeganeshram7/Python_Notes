package com.example.sample_java_assignment_app;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SpringbootSampleAppApplicationTests {

	@Test
	void testLoginMethod() {
		SpringbootSampleAppApplication app = new SpringbootSampleAppApplication();
		String result = app.login("test");
		assertEquals("Please input your credentials for login...", result);
	}

	@Test
	void testRegisterMethod() {
		SpringbootSampleAppApplication app = new SpringbootSampleAppApplication();
		String result = app.register("test");
		assertEquals("Please follow registration process...", result);
	}

}