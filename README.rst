prett: A Pretty Project Framework
==================================

.. image:: https://travis-ci.com/KD-Group/prett.svg?branch=master
    :target: https://travis-ci.com/KD-Group/prett

A pretty project framework for Python3 & PySide.

I hope it is useful for you, too. :D

============
Dict Storage
============

All the project items' values are stored in the **project.value** dict. The key is the item name.
Generally this dict can be serialized and stored in the file if the dict can be pickled directly.

.. code-block:: python

    import prett


    class ItemDemo(prett.IntProjectItem):
        pass

    class ProjectDemo(prett.AbstractProject):
        def __init__(self):
            self.width = ItemDemo(self)
            self.height = ItemDemo(self)

    p = ProjectDemo()
    p.width.int.value = 16
    p.height.int.value = 20
    print(p.value)  # {'width': '16', 'height': '20'}


===============
Type Conversion
===============

In prett, there are default type conversion in string-int and string-float.
When the item is inherited from StringIntItem, the item value is stored in string type, and its int property will automatically convert to or from string type.

.. code-block:: python

    import prett


    class ItemDemo(prett.IntProjectItem):
        pass

    class ProjectDemo(prett.AbstractProject):
        def __init__(self):
            self.length = ItemDemo(self)

    p = ProjectDemo()
    p.length.string.value = '200'
    print(p.length.int.value)  # 200, type is int

==============
Changed Signal
==============

When the value of property change, the changed signals of project, item, and properties will be emitted.

.. code-block:: python

    import prett


    class ItemDemo(prett.IntProjectItem):
        pass

    class ProjectDemo(prett.AbstractProject):
        def __init__(self):
            self.width = ItemDemo(self)
            self.height = ItemDemo(self)

    p = ProjectDemo()
    p.width.int.value = 16  # p.changed signal emitted, p.width.changed emitted
                            # then p.width.string.changed emitted, p.width.int.changed emitted
