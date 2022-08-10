from project.student_report_card import StudentReportCard

from unittest import TestCase, main

class StudentReportCardTests(TestCase):
    def setUp(self) -> None:
        student = StudentReportCard('Gosho', 10)

    def test_init_student_report_card(self):
        student_name = 'Gosho'
        school_year = 10
        student = StudentReportCard(student_name, school_year)

        self.assertEqual(student_name, student.student_name)
        self.assertEqual(school_year, student.school_year)
        self.assertEqual({}, student.grades_by_subject)

    def test_student_name_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            student = StudentReportCard('', 10)
        self.assertEqual('Student Name cannot be an empty string!', str(context.exception))

    def test_school_year_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            student = StudentReportCard('Gosho', 0)
        self.assertEqual('School Year must be between 1 and 12!', str(context.exception))

        with self.assertRaises(ValueError) as context:
            student = StudentReportCard('Gosho', 13)
        self.assertEqual('School Year must be between 1 and 12!', str(context.exception))

        student = StudentReportCard('Gosho', 8)
        self.assertTrue(8 in [int(x) for x in range(1, 13)])


    def test_add_grade_not_in_dict(self):













if __name__ == '__main__':
    main()
