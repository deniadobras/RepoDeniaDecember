def calsum(l):
    return sum([int(i) for i in l if type(i) == int or type(i) == float])

alist = [
    123.456,
    7,
    "abc",
    (1.2, 3),
    [
        [1, 2, 3.4],
        (5, 6.7, 9)
    ],
    (
        ("a", "3.68", 9),
        (10, 11.0, 12.3, "abc"),
        [1, 6]
    ),
    [
        [
            1.678903,
            {"a": "1, 2 '\"f': 1, {'a': 999} "},
            4.3301,
            {"b": [0, "1.33", 0.2, [1, 5, (6, 3, 0)]]},
            [
                {"c": [{"d": 0.4}, {"e": 4.5}, {"-23": [1, 2]}]},
                2,
                6.0004,
                "0",
                [
                    [1, 3, 6, 9.7],
                    ("f", 2.55)
                ]
            ]
        ],
        (1, 4, 0, "-1")
    ]
]

print(calsum(alist))