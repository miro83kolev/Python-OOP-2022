from unittest import TestCase, main

from workshop.internal_list import ListInternal


class ListInternalTests(TestCase):
    def test_append_when_list_is_empty(self):
        ll = ListInternal()
        value = 1
        result = ll.append(value)

        self.assertListEqual([value], list(ll))
        self.assertEqual(ll, result)

    def test_append_one_more_value(self):
        ll = ListInternal()
        values = [1, 2, 3]
        result = [ll.append(v) for v in values]

        self.assertListEqual(values, list(ll))
        self.assertEqual([ll] * len(values), result)

    def test_remove_when_value_exists_expected_to_be_removed(self):
        ll = ListInternal()
        value = 1
        index = 0
        ll.append(value)

        result = ll.remove(index)
        self.assertEqual(value, result)
        self.assertListEqual([], list(ll))


    def test_remove_single_element_expect_empty_list(self):
        ll = ListInternal()
        value = 1
        index = 0
        ll.append(value)

        result = ll.remove(index)
        self.assertEqual(value, result)
        self.assertListEqual([], list(ll))

    def test_remove_when_value_not_in_list(self):
        pass

    def test_extend_both_lists_have_values(self):
        pass

    def test_extend_when_first_list_is_empty(self):
        pass

    def test_extend_when_second_list_is_empty(self):
        pass

    def test_extend_when_both_lists_are_empty(self):
        pass







if __name__ == '__main__':
    main()