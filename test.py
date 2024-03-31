import unittest
import subprocess

class TestProgram(unittest.TestCase):
    def test_1(self):
        process = subprocess.Popen(['python', 'atm.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input='9681\n')
        print(stdout)
        self.assertIn('CORRECT PIN', stdout)
        print("Test 1 passed")

    def test_2(self):
        process = subprocess.Popen(['python', 'atm.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input='4321\n9681\n')
        outs = stdout.split('\n')
        self.assertIn('INCORRECT PIN', outs[0])
        self.assertIn('CORRECT PIN', outs[1])
        print("Test 2 passed")

    def test_3(self):
        process = subprocess.Popen(['python', 'atm.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input='4321ab\n43\n4321\n9681\n')
        outs = stdout.split('\n')
        self.assertIn('INVALID PIN FORMAT', outs[0])
        self.assertIn('INVALID PIN FORMAT', outs[1])
        self.assertIn('INCORRECT PIN', outs[2])
        self.assertIn('CORRECT PIN', outs[3])        
        print("Test 3 passed")

    def test_4(self):
        inputs = '0000\n0000\n0000\n1234\n'
        process = subprocess.Popen(['python', 'atm.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=inputs)
        outs = stdout.split('\n')
        for out in outs[:3]:
            self.assertIn('CORRECT PIN', out)
        self.assertIn('BANK CARD HELD', outs[3])
        print("Test 4 passed")

    def test_5(self):
        process = subprocess.Popen(['python', 'atm.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input='4321ab\n43\n00000\n12341\n')
        outs = stdout.split('\n')
        self.assertIn('INVALID PIN FORMAT', outs[0])
        self.assertIn('INVALID PIN FORMAT', outs[1])
        self.assertIn('INVALID PIN FORMAT', outs[2])
        self.assertIn('BANK CARD HELD', outs[3])
        print("Test 5 passed")


if __name__ == '__main__':
    unittest.main()
