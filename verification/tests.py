"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[True, True, False, True, False]],
            "answer": True
        },
        {
            "input": [[True, True, False]],
            "answer": True
        },
        {
            "input": [[True, True, False, False]],
            "answer": False
        },
        {
            "input": [[True, True, False, False, False]],
            "answer": False
        },
        {
            "input": [[False]],
            "answer": False
        },
        {
            "input": [[True]],
            "answer": True
        },
        {
            "input": [[]],
            "answer": False
        },
    ],
    "Extra": [
        {
            "input": [[False, False, True]],
            "answer": False
        },
        {
            "input": [[False, False, False]],
            "answer": False
        },
        {
            "input": [[True, True, True]],
            "answer": True
        },
    ]
}
