package org.sample;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorTest {

    @Test
    void testAdd() {
        Calculator calc = new Calculator();
        assertEquals(5, calc.add(2, 3));
    }

//    @Test
//    void testDivide() {
//        Calculator calc = new Calculator();
//        assertEquals(2, calc.divide(4, 2));
//    }
}
