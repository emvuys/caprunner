import unittest

from interpreter import ExecutionDone, JavaCardVM, JavaCardFrame, JavaCardLocals, JavaCardStack

class TestInterpreter(unittest.TestCase):

    def _func(self, intr, params, bytecodes):
        intr.frames.append(JavaCardFrame(params, bytecodes))
        

    def _run(self, intr):
        try:
            while True:
                intr.step()
        except ExecutionDone:
            pass

    def testEasy(self):
        intr = JavaCardVM(None)
        intr.frames.push(JavaCardFrame([None, 4],[]))
        intr.sload_1()
        intr.bspush(58)
        intr.sadd()
        intr.s2b()
        intr.sreturn()
        self.assertEquals(62, intr.getRetValue())

    def testSomeIf(self):
        intr = JavaCardVM(None)
        intr.frames.push(JavaCardFrame([None, 6], [29, 5, 73, 97, 6, 29, 6, 69, 120, 3, 49, 30, 29, 109, 13, 30, 8, 65, 48, 30, 4, 65, 91, 49, 112, 243, 29, 120]))
        self._run(intr)

    def test_gcdRecursif(self):
        intr = JavaCardVM(None)
        intr.frames.push(JavaCardFrame([42,56], [29, 97, 4, 28, 120, 29, 28, 29, 73, 141, 0, 7, 120]))
        self._run(intr)
        self.assertEquals(14, intr.getRetValue())
        

    def test_gcdIteratif(self):
        intr = JavaCardVM(None)
        intr.frames.push(JavaCardFrame([42,56], [29, 97, 4, 28, 120, 28, 29, 73, 49, 29, 47, 30, 48, 112, 243]))
        self._run(intr)
        self.assertEquals(14, intr.getRetValue())

class TestLocals(unittest.TestCase):
    def test_init(self):
        loc = JavaCardLocals(4,5,6,7,8)
        self.assertEqual(4, loc[0])
        self.assertEqual(5, len(loc))

        array = [1,2,3,4]
        loc = JavaCardLocals(*array)
        self.assertEqual(3, loc[2])
        self.assertEqual(4, len(loc))

    def test_getparams(self):
        loc = JavaCardLocals(self,2)
        self.assertTrue(loc.aget(0) is self)
        self.assertEquals(2, loc.sget(1))

    def test_getlocals(self):
        loc = JavaCardLocals(self)
        self.assertEqual(0, loc.sget(3))
        self.assertTrue(loc.aget(1) is None)

    def test_asArray(self):
        array = [89,3,None,7]
        loc = JavaCardLocals(*array)
        self.assertEqual(array, loc.asArray())

class TestStack(unittest.TestCase):
    def test(self):
        s = JavaCardStack()
        s.push(2)
        self.assertEquals(2, s.pop())
        
