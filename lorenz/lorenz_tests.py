import unittest
from unittest.mock import patch
from lorenz_attractor import fill_values, var_init, lorenz_plot

class TestLorenzSystem(unittest.TestCase):
    def setUp(self):
        x, y, z, t, s, r, b, Dt, xresult, yresult, zresult, timesteps = var_init()
        self.x, self.y, self.z, self.t, self.s, self.r, self.b, self.Dt, self.xresult, self.yresult, self.zresult, self.timesteps = fill_values(x, y, z, t, s, r, b, Dt, xresult, yresult, zresult, timesteps)

    def test_fill_values(self):
        self.assertEqual(len(self.xresult), 2)
        self.assertEqual(len(self.yresult), 2)
        self.assertEqual(len(self.zresult), 2)
        self.assertEqual(len(self.timesteps), 2)

        # self.assertEqual(self.xresult[1], x + (s * (y - x)) * Dt)
        # self.assertEqual(self.yresult[1], y + (r * x - y - x * z) * Dt)
        # self.assertEqual(self.zresult[1], z + (x * y - b * z) * Dt)

        self.assertEqual(self.xresult[1], 1)
        self.assertEqual(self.yresult[1], 1.28)
        self.assertEqual(self.zresult[1], 0.98)
    
    @patch('matplotlib.pyplot.show')
    def test_plot(self, mock_show):
        lorenz_plot(self.timesteps, self.xresult, self.yresult, self.zresult)
        mock_show.assert_called()

if __name__ == '__main__':
    unittest.main()
