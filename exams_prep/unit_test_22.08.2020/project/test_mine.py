from unittest import TestCase, main

from project.student_report_card import StudentReportCard


class StudentReportCardTests(TestCase):
    def setUp(self):
        self.student = StudentReportCard('Ivan', 8)

    def test_init_student_report_card(self):
        self.assertEqual('Ivan', self.student.student_name)
        self.assertEqual(8, self.student.school_year)
        self.assertDictEqual({}, self.student.grades_by_subject)

    def test_setter_name_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            self.student.student_name = ''
        self.assertEqual('Student Name cannot be an empty string!', str(context.exception))

    def test_school_year_set_up_with_valid_number(self):
        for grade in range(1, 13):
            self.student.school_year = grade
            self.assertEqual(grade, self.student.school_year)

    def test_setter_year_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            self.student.school_year = 0
        self.assertEqual('School Year must be between 1 and 12!', str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.student.school_year = 13
        self.assertEqual('School Year must be between 1 and 12!', str(context.exception))

    def test_add_grade_when_subject_not_present(self):
        subject = 'Math'
        result = self.student.grades_by_subject['Math'] = []
        self.assertEqual([], result)
        self.assertEqual(0, len(self.student.grades_by_subject['Math']))

    def test_add_grade_when_subject_present(self):
        subject = 'Math'
        self.student.grades_by_subject['Math'] = []
        self.assertEqual(0, len(self.student.grades_by_subject['Math']))
        subject = 'Math'
        grade = 5.50
        self.student.add_grade('Math', 5.50)
        self.assertEqual(1, len(self.student.grades_by_subject['Math']))
        self.assertIn(5.50, self.student.grades_by_subject['Math'])
        new_grade = 6
        self.student.add_grade('Math', 6)
        self.assertEqual(2, len(self.student.grades_by_subject['Math']))
        self.assertDictEqual({'Math': [5.50, 6]}, self.student.grades_by_subject)

    def test_average_grade_by_subject_report(self):
        subject = 'Math'
        grade_one = 5
        grade_two = 6
        grade_three = 4
        self.student.add_grade('Math', grade_one)
        self.student.add_grade('Math', grade_two)
        self.student.add_grade('Math', grade_three)
        self.assertEqual(3, len(self.student.grades_by_subject['Math']))
        average_grade = ((grade_one + grade_two + grade_three) / len(self.student.grades_by_subject['Math']))
        result = self.student.average_grade_by_subject()
        self.assertEqual(f'Math: 5.00', result)

    def test_average_all_subjects(self):
        self.student.grades_by_subject['Math'] = [6, 4, 6]
        self.student.grades_by_subject['English'] = [3, 4, 5]
        self.assertEqual(3, len(self.student.grades_by_subject['Math']))
        self.assertEqual(3, len(self.student.grades_by_subject['English']))
        sum_all_grade = sum(self.student.grades_by_subject['Math']) + sum(self.student.grades_by_subject['English'])
        all_count = len(self.student.grades_by_subject['Math']) + len(self.student.grades_by_subject['English'])
        result = self.student.average_grade_for_all_subjects()
        expected = f'Average Grade: {sum_all_grade / all_count :.2f}'
        self.assertEqual(result, expected)

    def test_average_grade_by_subject_returns_correct_string(self):
        self.student.add_grade("Math", 5)
        self.student.add_grade("Math", 6)
        self.student.add_grade("Bio", 4)
        self.student.add_grade("Bio", 6)
        expected = "Math: 5.50\nBio: 5.00"
        self.assertEqual(expected, self.student.average_grade_by_subject())

    def test_average_grade_for_all_subjects_returns_correct_string(self):
        self.student.add_grade("Math", 5)
        self.student.add_grade("Math", 6)
        self.student.add_grade("Bio", 4)
        self.student.add_grade("Bio", 6)
        expected = "Average Grade: 5.25"
        self.assertEqual(expected, self.student.average_grade_for_all_subjects())

    def test_repr_returns_correct_string(self):
        self.student.add_grade("Math", 5)
        self.student.add_grade("Math", 6)
        self.student.add_grade("Bio", 4)
        self.student.add_grade("Bio", 6)

        expected = "Name: Test\nYear: 5\n----------\nMath: 5.50\nBio: 5.00\n----------\nAverage Grade: 5.25"

        self.assertEqual(expected, repr(self.student))

if __name__ == '__main__':
    main()
