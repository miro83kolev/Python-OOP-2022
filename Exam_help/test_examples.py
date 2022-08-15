from unittest import TestCase, main

class TrainTests(TestCase):
    # set up of a train instance
    def setUp(self) -> None:
        self.train = Train("Test", 5)

    # checks train initialization
    def test_train_initialized_correctly(self):
        train = Train("Test", 10)
        self.assertEqual("Test", train.name)
        self.assertEqual(10, train.capacity)
        self.assertEqual([], train.passengers)

    # checks add method when full
    def test_add_passenger_capacity_full_raises(self):
        self.train.passengers = ["A", "B", "C", "D", "E"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("F")
        self.assertEqual("Train is full", str(ex.exception))

    # checks add method when passenger exists
    def test_add_passenger_that_already_exists_raises(self):
        self.train.passengers = ["A", "B", "C", "D"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("A")
        self.assertEqual("Passenger A Exists", str(ex.exception))

    # checks if passenger added correctly
    def test_add_passenger_adds_passenger_and_returns_correct_string(self):
        self.train.passengers = ["A", "B", "C"]
        result = self.train.add("D")
        self.assertEqual(["A", "B", "C", "D"], self.train.passengers)
        self.assertEqual("Added passenger D", result)

        result = self.train.add("E")
        self.assertEqual(["A", "B", "C", "D", "E"], self.train.passengers)
        self.assertEqual("Added passenger E", result)

    # checks if remove method raises error when passenger not existing
    def test_remove_passenger_who_does_not_exist_raises(self):
        self.train.passengers = ["A", "B", "C"]
        with self.assertRaises(ValueError) as ex:
            self.train.remove("D")
        self.assertEqual("Passenger Not Found", str(ex.exception))

    # checks if remove method correct
    def test_remove_passenger_removes_passenger_from_list(self):
        self.train.passengers = ["A", "B", "C"]
        result = self.train.remove("B")
        self.assertEqual(["A", "C"], self.train.passengers)
        self.assertEqual("Removed B", result)

    # checks add method when negative or zero quantity is added
    def test_add_food_with_negative_or_zero_quantity_raises(self):
        for quantity in range(-5, 0):
            with self.assertRaises(ValueError) as ex:
                self.pet_shop.add_food("dog food", quantity)
            self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    # checks if add method works and new food and its quantity is added to dict
    def test_add_food_adds_food_that_does_not_already_exist(self):
        self.pet_shop.add_food("Dog food", 10)
        self.assertEqual({"Dog food": 10}, self.pet_shop.food)

    # checks add food returns proper string
    def test_add_food_returns_correct_string(self):
        result = self.pet_shop.add_food("Dog food", 10)
        expected = "Successfully added 10.00 grams of Dog food."
        self.assertEqual(expected, result)

    # checks if adding to dict is correct
    def test_team_add_member_adds_correctly_if_name_not_in_members_dict(self):
        self.team.add_member(ana=20, eva=21)
        self.assertEqual({"ana": 20, "eva": 21}, self.team.members)
        self.team.add_member(ana=20)
        self.assertEqual({"ana": 20, "eva": 21}, self.team.members)

    # checks message when adding two team members to dict
    def test_team_add_member_returns_correct_string(self):
        result = self.team.add_member(ana=20, eva=21)
        self.assertEqual({"ana": 20, "eva": 21}, self.team.members)
        expected = "Successfully added: ana, eva"
        self.assertEqual(expected, result)

    # checks message when removing a team members from dict
    def test_remove_member_removes_if_member_in_members(self):
        self.team.add_member(ana=20, eva=21)
        result = self.team.remove_member("eva")
        self.assertEqual({"ana": 20}, self.team.members)
        self.assertEqual(f"Member eva removed", result)

    # checks message when removing a team members from dict and member does not exist
    def test_remove_member_if_member_not_in_members_returns_correct_string(self):
        self.team.add_member(ana=20)
        result = self.team.remove_member("eva")
        self.assertEqual(f"Member with name eva does not exist", result)

    # checks gt method with 2 teams
    def test_greater_than_method_returns_correctly(self):
        self.team.add_member(ana=20, eva=21)
        self.team2.add_member(peter=23)
        result = self.team > self.team2
        self.assertEqual(True, result)

        result = self.team < self.team2
        self.assertEqual(False, result)

        self.team2.add_member(george=25)
        result = self.team > self.team2
        self.assertEqual(False, result)

    # checks len method of 1 team
    def test_len_method_returns_correctly(self):
        self.team.add_member(ana=20, eva=21)
        result = len(self.team)
        self.assertEqual(2, result)

    # checks add method creates a combined ot 2 teams - name and dict
    def test_add_method_creates_new_instance_from_two_teams(self):
        self.team.add_member(ana=20, eva=21)
        self.team2.add_member(peter=23)
        new_team = self.team + self.team2
        self.assertEqual("TestTestTwo", new_team.name)
        self.assertEqual({"ana": 20, "eva": 21, "peter": 23}, new_team.members)

    # checks str method return properly
    def test_str_method_returns_correct_string(self):
        self.team.add_member(ana=20, eva=21, alice=21)
        result = str(self.team)
        expected = "Team name: Test\n" \
                   "Member: alice - 21-years old\n" \
                   "Member: eva - 21-years old\n" \
                   "Member: ana - 20-years old"
        self.assertEqual(expected, result)

    # checks adding to dict of lists
    def test_add_grade_adds_subject_that_does_not_exist_to_grades_by_subject(self):
        self.src.add_grade("Math", 5)
        expected = {"Math": [5]}
        self.assertEqual(expected, self.src.grades_by_subject)

    # checks average of 2 subjects added and print out
    def test_average_grade_by_subject_returns_correct_string(self):
        self.src.add_grade("Math", 5)
        self.src.add_grade("Math", 6)
        self.src.add_grade("Bio", 4)
        self.src.add_grade("Bio", 6)
        expected = "Math: 5.50\nBio: 5.00"
        self.assertEqual(expected, self.src.average_grade_by_subject())

    # checks average of all subjects
    def test_average_grade_for_all_subjects_returns_correct_string(self):
        self.src.add_grade("Math", 5)
        self.src.add_grade("Math", 6)
        self.src.add_grade("Bio", 4)
        self.src.add_grade("Bio", 6)
        expected = "Average Grade: 5.25"
        self.assertEqual(expected, self.src.average_grade_for_all_subjects())

    # checks repr output
    def test_repr_returns_correct_string(self):
        self.src.add_grade("Math", 5)
        self.src.add_grade("Math", 6)
        self.src.add_grade("Bio", 4)
        self.src.add_grade("Bio", 6)

        expected = "Name: Test\nYear: 5\n----------\nMath: 5.50\nBio: 5.00\n----------\nAverage Grade: 5.25"

        self.assertEqual(expected, repr(self.src))

    # checks when full raises error in range
    def test_planting_if_plantation_is_full_raises(self):
        self.plantation.size = 5
        self.plantation.hire_worker("Adam")
        for index in range(5):
            self.plantation.planting("Adam", "Tomato" + str(index))

        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Adam", "Tomato5")
        self.assertEqual("The plantation is full!", str(ex.exception))




if __name__ == "__main__":
    main()