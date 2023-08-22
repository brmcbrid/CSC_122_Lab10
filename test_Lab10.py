# Tests for Lab10
# Name Format

import os.path
import sys
from Lab10 import main
from tud_tests import *

def test_Lab10():

    try:
        exists = os.path.exists("Lab10.py")
        assert exists == True
    except:
        sys.exit()

    # Test 1
    set_keyboard_input(["Brian McBride"])
    main()
    output = get_display_output()

    assert output == [
        "Enter your name: ",
        "McBride, B."
        ]

    # Test 2
    set_keyboard_input(["Thomas Stearns Eliot"])
    main()
    output = get_display_output()

    assert output == [
        "Enter your name: ",
        "Eliot, T.S."
        ]
