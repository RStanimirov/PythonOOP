import unittest

from student.project.student import Student
# from project.student import Student


class StudentTests(unittest.TestCase):

    def test_init_no_courses(self):
        my_student = Student("Peter")
        self.assertEqual("Peter", my_student.name)
        self.assertEqual({}, my_student.courses)

    def test_init_with_courses(self):
        my_student = Student("Peter", "Mathematics")
        self.assertEqual("Peter", my_student.name)
        self.assertEqual("Mathematics", my_student.courses)

    def test_enroll_update_notes_when_course_existing(self):
        my_student = Student("Peter")
        my_student.enroll("Mathematics", ["a hard course"])
        result = my_student.enroll("Mathematics", ["a hard course indeed"])
        self.assertEqual(result, "Course already added. Notes have been updated.")

    def test_enroll_add_course_and_notes_when_course_note_is_Y(self):
        my_student = Student("Peter")
        result = my_student.enroll("DataScience", ["Statistics", "Combinatorics", "Hypothesis"], "Y")
        self.assertEqual(result, "Course and course notes have been added.")

    def test_enroll_add_course_and_notes_when_course_note_is_EmptyString(self):
        my_student = Student("Peter")
        result = my_student.enroll("ML", ["Sentiment Analysis", "Abnormalities Detection"], "")
        self.assertEqual(result, "Course and course notes have been added.")

    def test_enroll_add_new_course(self):
        my_student = Student("Peter")
        result = my_student.enroll("AI", ["TensorFlow.", "PyTorch", "Scikit Learn"], "AI")
        self.assertEqual(my_student.courses, {"AI": []})
        self.assertEqual(result, "Course has been added.")

    def test_add_notes_when_course_existing(self):
        my_student = Student("Peter")
        my_student.courses = {"MathForDevs": []}
        result = my_student.add_notes("MathForDevs", ["Calculus", "Statistics", "High School Math"])
        self.assertEqual(result, "Notes have been updated")

    def test_add_notes_when_course_not_existing(self):
        my_student = Student("Peter")
        with self.assertRaises(Exception) as ex:
            my_student.add_notes("MathForDevs", ["Calculus", "Statistics", "High School Mat"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_courses_when_course_existing(self):
        my_student = Student("Peter")
        my_student.courses = {"MathForDevs": []}
        result = my_student.leave_course("MathForDevs")
        self.assertEqual(result, "Course has been removed")

    def test_leave_courses_when_course_not_existing(self):
        my_student = Student("Peter")
        with self.assertRaises(Exception) as ex:
            my_student.leave_course("MathForDevs")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    unittest.main()