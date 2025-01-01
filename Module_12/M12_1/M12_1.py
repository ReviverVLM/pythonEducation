"""
Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:

test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
Далее вызовите метод walk у этого объекта 10 раз.
После чего методом assertEqual сравните distance этого объекта со значением 50.

test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
Далее вызовите метод run у этого объекта 10 раз.
После чего методом assertEqual сравните distance этого объекта со значением 100.

test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
Далее 10 раз у объектов вызываются методы run и walk соответственно.
Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.

Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.
"""

import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def setUp(self):
        self.runner = Runner("Супер-ёжик Соник")  # (не из фильма)
        self.runner2 = Runner("Тейлз")

    def test_walk(self):
        for _ in range(10): self.runner.walk()
        self.assertEqual(self.runner.distance, 50)

    def test_run(self):
        for _ in range(10): self.runner.run()
        self.assertEqual(self.runner.distance, 100)

    def test_challenge(self):
        for _ in range(10): self.runner.run()
        for _ in range(10): self.runner2.walk()
        self.assertNotEqual(self.runner.distance, self.runner2.distance)


if __name__ == '__main__':
    unittest.main()
