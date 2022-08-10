from project.team import Team

from unittest import TestCase, main


class TeamTest(TestCase):

    def test_init_team(self):
        team_name = 'Test'
        team = Team(team_name)

        self.assertEqual(team_name, team.name)
        self.assertDictEqual({}, team.members)

    def test_property_name_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            team = Team('123asdASD,.#@%&')
        self.assertEqual('Team Name can contain only letters!', str(context.exception))

    def test_add_team_member_successfully(self):
        team = Team('Test')
        team.members['ivan'] = 18
        result = team.add_member(gosho=13, ivan=18, josh=21, stoyan=25)
        self.assertEqual(f'Successfully added: gosho, josh, stoyan', result)
        self.assertEqual(13, team.members['gosho'])
        self.assertEqual(18, team.members['ivan'])
        self.assertEqual(21, team.members['josh'])
        self.assertEqual(25, team.members['stoyan'])

    def test_remove_existing_member(self):
        team = Team('Test')
        team_member = 'Pesho'
        team.members[team_member] = 18
        self.assertTrue(team_member in team.members)
        result = team.remove_member(team_member)
        self.assertEqual(f"Member {team_member} removed", result)
        self.assertTrue(team_member not in team.members)

    def test_remove_not_existing_member(self):
        team = Team('Test')
        name = 'Pesho'
        result = team.remove_member(name)
        expected = f'Member with name {name} does not exist'
        self.assertEqual(expected, result)
        self.assertTrue(name not in team.members)

    def test_gt_returns_correct_answer(self):
        team_one = Team('Test')
        team_two = Team('Me')
        team_one.add_member(Pesho=18, Gosho=20)
        team_two.add_member(Ivan=30)
        self.assertTrue(2, team_one.members.__len__())
        self.assertTrue(1, team_two.members.__len__())
        result = team_one > team_two
        result_one = team_one < team_two
        self.assertEqual(result, True)
        self.assertFalse(result_one, False)

    def test_len_members_return_correct(self):
        team = Team('Test')
        member = 'Pesho'
        member_two = 'Gosho'
        team.members[member] = 18
        team.members[member_two] = 20
        self.assertEqual(2, team.members.__len__())
        team.remove_member(member)
        self.assertEqual(1, team.members.__len__())

    def test_add_method(self):
        team_one = Team('Test')
        team_two = Team('Me')
        team_one.add_member(Pesho=18, Gosho=20)
        team_two.add_member(Ivan=30)
        result = team_one + team_two
        expected_result_members = {'Pesho': 18, 'Gosho': 20, 'Ivan': 30}
        self.assertEqual('TestMe', result.name)
        self.assertEqual(expected_result_members, result.members)

    def test_str_method_correct_answer(self):
        team = Team('Test')
        team.members['ivan'] = 20
        team.members['gosho'] = 35
        team.members['stoyan'] = 17

        result = str(team)
        expected = f'Team name: Test\n' + \
            f'Member: gosho - 35-years old\n' + \
            f'Member: ivan - 20-years old\n' + \
            f'Member: stoyan - 17-years old'

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
