from unittest import TestCase, main

from student.project.student import Student


class StudentTests(TestCase):
    def setUp(self):
        self.student = Student('John', {'Web programming': ['note1', 'note2'],
                                        'JS programming': ['note3', 'note4']})

    def test_init_only_with_name(self):
        name = 'John'
        student = Student(name)

        self.assertEqual(name, student.name)
        self.assertEqual({}, student.courses)

    def test_init_only_with_courses(self):
        name = 'John'
        courses = {'Web programming': ['note1', 'note2'], 'JS programming': ['note3', 'note4']}
        student = Student(name, courses)

        self.assertEqual(name, student.name)
        self.assertEqual(courses, student.courses)

    def test_enroll_with_already_enrolled_course_add_notes(self):
        new_notes = ['new note']
        course = 'JS programming'

        expected_notes = self.student.courses[course] + new_notes

        result = self.student.enroll(course, ['new note'])
        self.assertEqual('Course already added. Notes have been updated.', result)
        self.assertEqual(expected_notes, self.student.courses[course])


    def test_enroll_with_new_course_add_notes_empty_string(self):
        course = 'Database Basics'
        notes = ['F1', 'F2']

        result = self.student.enroll(course, notes, '')
        self.assertEqual('Course and course notes have been added.', result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_with_new_course_add_notes_y_string(self):
        course = 'Database Basics'
        notes = ['F1', 'F2']

        result = self.student.enroll(course, notes, 'Y')
        self.assertEqual('Course and course notes have been added.', result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_new_course_no_notes(self):
        course = 'Database Basics'
        notes = ['F1', 'F2']

        result = self.student.enroll(course, notes, 'N')
        self.assertEqual('Course has been added.', result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual([], self.student.courses[course])

    def test_add_notes_in_existing_course(self):
        course = 'JS programming'
        result = self.student.add_notes(course, 'extra note')

        self.assertEqual('Notes have been updated', result)
        self.assertEqual(['note3', 'note4', 'extra note'], self.student.courses[course])

    def test_add_notes_raises(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes('Invalid course', 'random note')
        self.assertEqual('Cannot add notes. Course not found.', str(context.exception))

    def test_leave_course_remove_from_student(self):
        course = 'JS programming'
        result = self.student.leave_course(course)

        self.assertEqual('Course has been removed', result)
        self.assertTrue(course not in self.student.courses)
        self.assertTrue(len(self.student.courses) > 0)

    def test_leave_raises_when_course_does_not_exist(self):
        with self.assertRaises(Exception) as context:
            self.student.leave_course('Invalid course')
        self.assertEqual('Cannot remove course. Course not found.', str(context.exception))



if __name__ == '__main__':
    main()