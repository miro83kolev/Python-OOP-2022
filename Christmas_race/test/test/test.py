from project.team import Team
from unittest import TestCase, main


class TeamTests(TestCase):

    def setUp(self) -> None:
        self.team = Team('Team')

    def test_team_init(self):
        team_name = 'Team'
        team = Team(team_name)

        self.assertEqual(team_name, team.name)
        self.assertEqual({}, team.members)

    def test_setter_raises(self):
        with self.assertRaises(ValueError) as context:
            team = Team('1234HGAw..0#@')
        self.assertEqual('Team Name can contain only letters!', str(context.exception))

    def test_add_member_new_player(self):
        self.team.members['ivan'] = 18
        result = self.team.add_member(ivan=18, gosho=21, pesho=22)

        self.assertEqual('Successfully added: gosho, pesho', result)
        self.assertEqual(21, self.team.members['gosho'])
        self.assertEqual(22, self.team.members['pesho'])

    def test_remove_member_error_message_not_existing(self):
        result = self.team.remove_member('pesho')
        self.assertEqual(f"Member with name pesho does not exist", result)

    def test_remove_member_when_existing_member(self):
        self.team.members['pesho'] = 18
        self.team.members['gosho'] = 20
        result = self.team.remove_member('gosho')
        self.assertEqual(f"Member gosho removed", result)
        self.assertEqual(18, self.team.members['pesho'])
        self.assertTrue('gosho' not in self.team.members)

    def test_gt_compares_team_by_count(self):
        self.team.members['member1'] = 18
        self.team.members['member2'] = 19

        another_team = Team('Another')
        another_team.members['member1'] = 21
        another_team.members['member2'] = 22
        another_team.members['member3'] = 23

        self.assertEqual(True, another_team > self.team)
        self.assertFalse(False, self.team > another_team)

    def test_len_returns_members_count(self):
        self.team.members['member1'] = 18
        self.team.members['member2'] = 19

        self.assertEqual(2, len(self.team))

    def test_add_merge_two_teams(self):
        self.team.members['member1'] = 18
        self.team.members['member2'] = 19

        another_team = Team('Another')
        another_team.members['member3'] = 21
        another_team.members['member4'] = 22
        another_team.members['member5'] = 23

        result = self.team + another_team
        expected_members = {
            'member1': 18,
            'member2': 19,
            'member3': 21,
            'member4': 22,
            'member5': 23
        }
        self.assertEqual('TeamAnother', result.name)
        self.assertEqual(expected_members, result.members)

    def test_str_members_sort(self):
        self.team.members['member1'] = 18
        self.team.members['member3'] = 20
        self.team.members['member2'] = 19

        result = str(self.team)
        expected = f'Team name: Team\n' + \
            f'Member: member3 - 20-years old\n' + \
            f'Member: member2 - 19-years old\n' + \
            f'Member: member1 - 18-years old'

        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()
