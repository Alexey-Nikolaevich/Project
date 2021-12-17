import unittest
from pygame import Vector2
from Settings import*
from Bird import Bird

class TestBird(unittest.TestCase):

    def test_get_pos(self):
        bird = Bird()
        result = bird.get_pos()

        self.assertEqual(result, bird.pos)

    def test_get_vel(self):
        bird = Bird()
        result = bird.get_vel()

        self.assertEqual(result, bird.vel)

    def test_get_color(self):
        bird = Bird()
        result = bird.get_color()

        self.assertEqual(result, bird.color)

    def test_push(self):
        bird = Bird()
        Force = Vector2()
        initial_vel = bird.vel
        bird.push(Force)

        self.assertAlmostEqual(bird.vel,initial_vel + Force)
    
        
    def test_move(self):
        bird = Bird()
        result = bird.cage(bird.pos + bird.vel)

        bird.move()

        self.assertEqual(bird.pos, result)

    def test_cage(self):
        bird = Bird()

        bird.pos = bird.cage(Vector2(0,0))
        self.assertEqual(bird.pos, Vector2(0,0))

        bird.pos = bird.cage(Vector2(-1,0))
        self.assertEqual(bird.pos, Vector2(WIDTH,0))

        bird.pos = bird.cage(Vector2(0,-1))
        self.assertEqual(bird.pos, Vector2(0,HEIGHT))

        bird.pos = bird.cage(Vector2(-1,-1))
        self.assertEqual(bird.pos, Vector2(WIDTH,HEIGHT))
         

if __name__ == '__main__':
    unittest.main()