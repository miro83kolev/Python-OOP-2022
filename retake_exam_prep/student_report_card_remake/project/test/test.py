from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class StudentReportCardTests(TestCase):
    def setUp(self):
        self.student_report_card = StudentReportCard('Ivan', 5)

    def test_init_student_report_card(self):
        self.assertEqual('Ivan', self.student_report_card.student_name)
        self.assertEqual(5, self.student_report_card.school_year)
        self.assertEqual({}, self.student_report_card.grades_by_subject)
        self.assertEqual(0, len(self.student_report_card.grades_by_subject))

    def test_name_raises_ex(self):
        with self.assertRaises(ValueError) as ex:
            self.student_report_card.student_name = ''
            # StudentReportCard('', 5)
        self.assertEqual('Student Name cannot be an empty string!', str(ex.exception))

    def test_school_year_raises_ex(self):
        with self.assertRaises(ValueError) as ex:
            self.student_report_card.school_year = -1
            # StudentReportCard('Ivan', -1)
        self.assertEqual('School Year must be between 1 and 12!', str(ex.exception))

    def test_school_year_raises_ex_over_12(self):
        with self.assertRaises(ValueError) as ex:
            self.student_report_card.school_year = 13
            # StudentReportCard('Ivan', 13)
        self.assertEqual('School Year must be between 1 and 12!', str(ex.exception))

    def test_school_year_correct(self):
        for grade in range(1, 13):
            self.student_report_card.school_year = grade
            self.assertEqual(grade, self.student_report_card.school_year)

    def test_adds_subject_to_student_report_card(self):
        self.assertEqual(0, len(self.student_report_card.grades_by_subject))
        self.student_report_card.add_grade('Math', 5)
        self.assertEqual(1, len(self.student_report_card.grades_by_subject))
        self.assertTrue('Math' in self.student_report_card.grades_by_subject)
        self.student_report_card.add_grade('Math', 6)
        expected = {'Math': [5, 6]}
        result = self.student_report_card.grades_by_subject
        self.assertEqual(expected, result)

    def test_average_grade_by_subject_returns_correctly(self):
        self.student_report_card.add_grade('Math', 5)
        self.student_report_card.add_grade('Math', 6)
        self.student_report_card.add_grade('Bio', 6)
        self.student_report_card.add_grade('Bio', 6)
        expected = "Math: 5.50\nBio: 6.00"
        result = self.student_report_card.average_grade_by_subject()
        self.assertEqual(expected, result)

    def test_average_all_subjects_returns_correctly(self):
        self.student_report_card.add_grade('Math', 5)
        self.student_report_card.add_grade('Math', 6)
        self.student_report_card.add_grade('Bio', 6)
        self.student_report_card.add_grade('Bio', 6)
        result = self.student_report_card.average_grade_for_all_subjects()
        expected = "Average Grade: 5.75"
        self.assertEqual(expected, result)

    def test_repr_returns_correct(self):
        self.student_report_card.add_grade('Math', 5)
        self.student_report_card.add_grade('Math', 6)
        self.student_report_card.add_grade('Bio', 6)
        self.student_report_card.add_grade('Bio', 6)
        result = repr(self.student_report_card)
        expected = f'Name: Ivan\nYear: 5\n----------\nMath: 5.50\nBio: 6.00\n----------\nAverage Grade: 5.75'
        self.assertEqual(expected, result)









if __name__ == '__main__':
    main()
