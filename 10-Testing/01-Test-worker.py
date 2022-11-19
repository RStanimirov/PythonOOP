# RS modified github code in order to get 100/100 in judge. The original github code got only 83/100
# because there was no self.assertEqual("Not enough energy.", str(ex.exception))
import unittest


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTest(unittest.TestCase):
    # 1) Test if the worker is initialized with correct name, salary and energy
    def test_worker_name_salary_energy(self):
        worker = Worker("Peter", 2500, 100)
        self.assertEqual("Peter", worker.name)
        self.assertEqual(2500, worker.salary)
        self.assertEqual(100, worker.energy)

    # 2) Test if the worker's energy is incremented after the rest method is called
    def test_worker_energy_incrementation(self):
        worker = Worker("Peter", 2500, 100)
        worker.rest()
        self.assertEqual(100 + 1, worker.energy)

    # 3) Test if an error is raised if the worker tries to work with negative energy
    def test_worker_negative_energy(self):
        worker = Worker("Peter", 2500, -1)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    # 4) Test if an error is raised if the worker tries to work with energy equal to 0
    def test_worker_zero_energy(self):
        worker = Worker("Peter", 2500, 0)
        with self.assertRaises(Exception):
            worker.work()

    # 5) Test if the worker's money is increased by his salary correctly after the work method is called
    def test_worker_salary_increase(self):
        worker = Worker("Peter", 2500, 100)
        worker.work()
        self.assertEqual(2500, worker.money)
        worker.work()
        self.assertEqual(5000, worker.money)

    # 6 Test if the worker's energy is decreased after the work method is called
    def test_worker_energy_decrease(self):
        worker = Worker("Peter", 2500, 100)
        worker.work()
        self.assertEqual(100 - 1, worker.energy)

    # 7) Test if the get_info method returns the proper string with correct values
    def test_worker_get_info_method(self):
        worker = Worker("Peter", 2500, 100)
        expected = "Peter has saved 0 money."
        actual = worker.get_info()
        self.assertEqual(expected, actual)
        worker.work()
        expected = "Peter has saved 2500 money."
        actual = worker.get_info()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
