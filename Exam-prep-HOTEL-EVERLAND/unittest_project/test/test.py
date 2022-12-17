from unittest_project.student_report_card import StudentReportCard
import unittest


class Test(unittest.TestCase):
    # def setUp(self) -> None:
    #     self.rs_report_card = StudentReportCard("RS", 11)

    def test_1_init(self):
        rs_report_card = StudentReportCard("RS", 11)
        self.assertEqual("RS", rs_report_card.student_name)
        self.assertEqual(11, rs_report_card.school_year)
        self.assertEqual({}, rs_report_card.grades_by_subject)

    def test_2_name_empty_str(self):
        with self.assertRaises(ValueError) as ex:
            rs_report_card = StudentReportCard("", 11)
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_3_year_between_1_12(self):
        with self.assertRaises(ValueError) as ex:
            rs_report_card = StudentReportCard("RS", 22)
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_4_add_grade(self):
        rs_report_card = StudentReportCard("RS", 11)
        self.assertEqual({}, rs_report_card.grades_by_subject)
        rs_report_card.add_grade("Math", 5.20)
        self.assertEqual([5.20], rs_report_card.grades_by_subject["Math"])
        self.assertEqual({'Math': [5.20]}, rs_report_card.grades_by_subject)
        rs_report_card.add_grade("Math", 5.60)
        self.assertEqual([5.20, 5.60], rs_report_card.grades_by_subject["Math"])
        self.assertEqual({'Math': [5.20, 5.60]}, rs_report_card.grades_by_subject)
        rs_report_card.add_grade("Geog", 4.50)
        self.assertEqual({'Math': [5.20, 5.60], 'Geog': [4.50]}, rs_report_card.grades_by_subject)

    def test_4_add_grade_if_empty(self):
        rs_report_card = StudentReportCard("RS", 11)
        self.assertEqual({}, rs_report_card.grades_by_subject)
        rs_report_card.add_grade("Math", 5.20)
        self.assertEqual({'Math': [5.20]}, rs_report_card.grades_by_subject)
        self.assertEqual(1, len(rs_report_card.grades_by_subject))

    def test_4_add_grade_if_not_empty(self):
        rs_report_card = StudentReportCard("RS", 11)
        self.assertEqual({}, rs_report_card.grades_by_subject)
        rs_report_card.add_grade("Math", 5.20)
        rs_report_card.add_grade("Math", 5.60)
        self.assertEqual({'Math': [5.20, 5.60]}, rs_report_card.grades_by_subject)
        self.assertEqual(1, len(rs_report_card.grades_by_subject))

    def test_5_av_grade_by_subject(self):
        rs_report_card = StudentReportCard("RS", 11)
        rs_report_card.add_grade("Math", 5.20)
        rs_report_card.add_grade("Math", 5.60)
        rs_report_card.add_grade("Geog", 4.50)
        self.assertEqual({'Math': [5.2, 5.6], 'Geog': [4.5]}, rs_report_card.grades_by_subject)
        self.assertEqual(2, len(rs_report_card.grades_by_subject))

        average_grade = 0
        for k, v in rs_report_card.grades_by_subject.items():
            average_grade = sum(v) / len(v)
        self.assertEqual(average_grade, 4.50)
        test_res = "Math: 5.40\nGeog: 4.50\n"
        self.assertEqual(test_res.strip(), rs_report_card.average_grade_by_subject())

    def test_6_av_grade_for_all_subjects(self):
        rs_report_card = StudentReportCard("RS", 11)
        rs_report_card.add_grade("Math", 5.20)
        rs_report_card.add_grade("Math", 5.60)
        rs_report_card.add_grade("Geog", 4.50)
        sum_all_grades = 0
        all_count = 0
        av_grade = 0
        for x in rs_report_card.grades_by_subject.values():
            sum_all_grades += sum(x)
            all_count += len(x)
            av_grade = sum_all_grades / all_count
        self.assertEqual(sum_all_grades, 15.30)
        self.assertEqual(all_count, 3)
        self.assertEqual(av_grade, 5.1000000000000005)
        test_res = "Average Grade: 5.10"
        self.assertEqual(test_res, rs_report_card.average_grade_for_all_subjects())

    def test_7_repr(self):
        rs_report_card = StudentReportCard("RS", 11)
        rs_report_card.add_grade("Math", 5.20)
        rs_report_card.add_grade("Math", 5.60)
        rs_report_card.add_grade("Geog", 4.50)
        result = "Name: RS\nYear: 11\n----------\nMath: 5.40\nGeog: 4.50\n----------\nAverage Grade: 5.10"
        self.assertEqual(result, repr(rs_report_card))


if __name__ == '__main__':
    unittest.main()
