from project.team import Team

from unittest import TestCase, main

class TeamTests(TestCase):
    def setUp(self) -> None:
        self.team = Team('Test')
        self.team2 = Team('Other')

    def test_init_team(self):
        self.assertEqual('Test', self.team.name)
        self.assertEqual({}, self.team.members)
        self.assertEqual(0, len(self.team.members))

    def test_name_accepts_isalpha_and_raises_ex(self):
        with self.assertRaises(ValueError) as ex:
            self.team.name = 'Test1'
        self.assertEqual('Team Name can contain only letters!', str(ex.exception))

    def test_add_method_adds_not_existing_member_correctly(self):
        self.team.add_member(Ivan=21, Sotir=20)
        self.assertEqual({"Ivan": 21, "Sotir": 20}, self.team.members)
        self.assertEqual(2, len(self.team.members))
        self.team.add_member(Ivan=21)
        self.assertEqual({"Ivan": 21, "Sotir": 20}, self.team.members)
        self.assertEqual(2, len(self.team.members))

    def test_add_method_returns_correct_string(self):
        result = self.team.add_member(Ivan=21, Sotir=20)
        self.assertEqual({"Ivan": 21, "Sotir": 20}, self.team.members)
        expected = "Successfully added: Ivan, Sotir"
        self.assertEqual(expected, result)

    def test_removes_correctly_team_member(self):
        self.team.add_member(Ivan=21, Sotir=20)
        self.assertEqual({"Ivan": 21, "Sotir": 20}, self.team.members)
        self.assertEqual(2, len(self.team.members))
        result = self.team.remove_member('Ivan')
        self.assertEqual({"Sotir": 20}, self.team.members)
        self.assertEqual(1, len(self.team.members))
        self.assertTrue('Ivan' not in self.team.members)

    def test_removes_error_message_if_member_does_exists(self):
        self.team.add_member(Ivan=21, Sotir=20)
        self.assertEqual({"Ivan": 21, "Sotir": 20}, self.team.members)
        self.assertEqual(2, len(self.team.members))
        result = self.team.remove_member('John')
        expected = 'Member with name John does not exist'
        self.assertEqual(expected, result)
        self.assertEqual({"Ivan": 21, "Sotir": 20}, self.team.members)
        self.assertEqual(2, len(self.team.members))
        self.assertTrue('John' not in self.team.members)

    def test_len_method(self):
        self.assertEqual(0, len(self.team.members))
        self.team.add_member(ana=20, eva=21)
        result = len(self.team)
        self.assertEqual(2, result)

    def test_gt_method_returns_correctly(self):
        self.team.add_member(Ivan=21, Sotir=20)
        self.team2.add_member(Joro=18)
        result = self.team > self.team2
        self.assertEqual(True, result)

        self.team2.add_member(John=30)
        result = self.team > self.team2
        self.assertEqual(False, result)

    def test_add_method_correctly(self):
        self.team.add_member(Ivan=21, Sotir=20)
        self.team2.add_member(Joro=18)
        new_team = self.team + self.team2
        self.assertEqual("TestOther", new_team.name)
        self.assertEqual({'Ivan': 21, 'Sotir': 20, 'Joro': 18}, new_team.members)

    def test_str_method(self):
        self.team.add_member(Ivan=21, Sotir=20, Ana=20)
        result = str(self.team)
        expected = "Team name: Test\n" \
                   "Member: Ivan - 21-years old\n" \
                   "Member: Ana - 20-years old\n" \
                   "Member: Sotir - 20-years old"
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()