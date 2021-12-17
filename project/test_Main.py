import unittest
from unittest.signals import installHandler
import Main
from Bird import Bird
from pygame import Vector2
from Settings import*


class TestMain(unittest.TestCase):

    def test_rule1(self):
        this_bird = Bird()
        other_bird = Bird ()
        
        x = 1
        y = 1
        this_bird.vel = Vector2(x, y) 
        Main.rule1(this_bird, other_bird)
        self.assertNotEqual(this_bird.vel, Vector2(x, y))


    def test_rule2(self):
        this_bird = Bird()
        other_bird = Bird ()
        
        x = 1
        y = 1
        this_bird.vel = Vector2(x, y) 
        Main.rule2(this_bird, other_bird)
        self.assertNotEqual(this_bird.vel, Vector2(x, y))

    def test_rulee3(self):
        this_bird = Bird()
        other_bird = Bird ()
        
        x = 1
        y = 1
        this_bird.vel = Vector2(x, y) 
        Main.rule3(this_bird, other_bird)
        self.assertNotEqual(this_bird.vel, Vector2(x, y))

    def test_detect(self):
        this_bird = Bird()
        other_bird = Bird()

        this_bird.pos = Vector2(0,0)
        other_bird.pos = Vector2(1,0)
        Result = Main.detect(this_bird, other_bird)
        self.assertTrue(Result)

        this_bird.pos = Vector2(0,0)
        other_bird.pos = Vector2(VIEW_DISTANCE + 1,0)
        Result = Main.detect(this_bird, other_bird)
        self.assertFalse(Result)

        this_bird.pos = Vector2(0,0)
        other_bird.pos = Vector2(0,VIEW_DISTANCE + 1)
        Result = Main.detect(this_bird, other_bird)
        self.assertFalse(Result)

    
if __name__ == '__main__':
    unittest.main()