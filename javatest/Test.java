package javatest;
import javacard.framework.*;

public class Test extends Applet{

    short blah = 0;

    public static void install (byte[] bArray, short bOffset, byte bLength){
	new Test().register();
    }

    public void process(APDU apdu) throws ISOException{
	if (false) testCallAnotherFunction();
	ISOException.throwIt(ISO7816.SW_FUNC_NOT_SUPPORTED);
	testCallAnotherFunction();
    }

    public byte testfinally(byte a){
	try {
	    return (byte)(a+5);
	} finally {
	    return 5;
	}
    }

    public byte testEasy(byte a){
	return (byte)(a+58);
    }

    public short testSomeIf(short a){
	if ((a % 2) == 0){
	    return (short)(a * 3);
	} else {
	    for (byte i = 0; i < a; i++){
		a = (short)(i+5);
	    }
	    return a;
	}
    }

    public short accessField(short var){
	blah = (short)(var + blah);
	return (short)(blah * 2);
    }

    public void testLocalVariable(){
	byte a = 5;
	short [] b = new short[25];
    }

    public void testCallAnotherFunction(){
	accessField(blah);
    }

    static public short gcdIteratif(short u, short v){
	while (true) {
	    if (v == 0) {
		return u;
	    }
	    else {
		short r = (short)(u % v);
		u = v;
		v = r;
	    }
	}
    }

    static public short gcdRecursif(short u, short v){
	if (v == 0) {
	    return u;
	}
	else {
	    return gcdRecursif(v, (short)(u % v));
	}
    }

    public static void testStatic(){
	short a = 3;
    }

}