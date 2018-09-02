import unittest

import prett


class MyTestCase(unittest.TestCase):
    def test_dict_item_emit_change_condition(self):
        class ProjectDemo(prett.AbstractProject):
            def __init__(self):
                self.d = prett.DictProjectItem(self)

        p = ProjectDemo()
        self.emit_value = None

        @prett.connect_with(p.d.changed)
        def copy_value_from_dict_item(data: dict):
            self.emit_value = data.copy()

        # emit changed if use `=` operator
        p.d.dict.value = {1: 2, 3: 4}
        self.assertEqual(self.emit_value, {1: 2, 3: 4})

        # can't emit change if modify value directly
        p.d.dict.value.pop(1)
        self.assertEqual(self.emit_value, {1: 2, 3: 4})
        self.assertEqual(p.d.dict.value, {3: 4})

        # can't emit changed if assign reference origin value to value
        p.d.dict.value = {1: 2, 3: 4}
        self.assertEqual(self.emit_value, {1: 2, 3: 4})
        d = p.d.dict.value  # reference value
        d.pop(1)
        p.d.dict.value = d
        self.assertEqual(self.emit_value, {1: 2, 3: 4})

        # emit changed if you copy origin value, change it and assign to value
        p.d.dict.value = {1: 2, 3: 4}
        d = p.d.dict.value.copy()  # reference value
        d.pop(1)
        p.d.dict.value = d
        self.assertEqual(self.emit_value, {3: 4})

        # emit change if using DictProjectItem method
        p.d.dict.value = {1: 2, 3: 4}
        p.d.dict.pop(1)
        self.assertEqual(self.emit_value, {3: 4})

    def test_list_item_emit_change_condition(self):
        class ProjectDemo(prett.AbstractProject):
            def __init__(self):
                self.ls = prett.ListProjectItem(self)

        p = ProjectDemo()
        self.emit_value = None

        @prett.connect_with(p.ls.changed)
        def copy_value_from_dict_item(data: list):
            self.emit_value = data.copy()

        # emit changed if use `=` operator
        p.ls.list.value = [1, 2, 3, 4]
        self.assertEqual(self.emit_value, [1, 2, 3, 4])

        # can't emit change if modify value directly
        p.ls.list.value.pop(0)
        self.assertEqual(self.emit_value, [1, 2, 3, 4])
        self.assertEqual(p.ls.list.value, [2, 3, 4])

        # can't emit changed if assign reference origin value to value
        p.ls.list.value = [1, 2, 3, 4]
        self.assertEqual(self.emit_value, [1, 2, 3, 4])
        d = p.ls.list.value  # reference value
        d.pop(1)
        p.ls.list.value = d
        self.assertEqual(self.emit_value, [1, 2, 3, 4])

        # emit changed if you copy origin value, change it and assign to value
        p.ls.list.value = [1, 2, 3, 4]
        d = p.ls.list.value.copy()  # reference value
        d.pop(0)
        p.ls.list.value = d
        self.assertEqual(self.emit_value, [2, 3, 4])

        # emit change if using DictProjectItem method
        p.ls.list.value = [1, 2, 3, 4]
        p.ls.list.pop(0)
        self.assertEqual(self.emit_value, [2, 3, 4])


if __name__ == '__main__':
    unittest.main()
