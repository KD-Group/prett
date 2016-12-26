prett: A Pretty Project Framework
==================================

.. image:: https://travis-ci.org/SF-Zhou/prett.svg?branch=master
    :target: https://travis-ci.org/SF-Zhou/prett

.. image:: https://app.wercker.com/status/cbcc4fcd9f4ca96debab6a2ec90a0b9b/s/master
    :target: https://app.wercker.com/project/byKey/cbcc4fcd9f4ca96debab6a2ec90a0b9b

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
