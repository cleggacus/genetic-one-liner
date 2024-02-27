import random

def gen(val = list(map(lambda _: list(map(lambda _: random.randint(0,7),range(8))),range(50)))):
    return sorted(
        list(map(
            lambda x:[
                sum(
                    list(map(
                        lambda i: int(i%8 != i//8 and x[i//8] == x[i%8]) + 
                            int(i%8 != i//8 and abs(i%8 - i//8) == abs(x[i%8] - x[i//8])),
                        range(8*8)
                    ))
                ),
                x
            ],
            val
        )),
        key=lambda x:x[0]
    )[0][1] if sorted(
        list(map(
            lambda x:[
                sum(
                    list(map(
                        lambda i: int(i%8 != i//8 and x[i//8] == x[i%8]) + 
                            int(i%8 != i//8 and abs(i%8 - i//8) == abs(x[i%8] - x[i//8])),
                        range(8*8)
                    ))
                ),
                x
            ],
            val
        )),
        key=lambda x:x[0]
    )[0][1] else gen(
        list(map(
            lambda x: list(map(
                lambda x: int(x[0] < 0.02) * random.randint(0, 7) + int(x[0] >= 0.02) * x[1],
                x
            )),
            list(map(
                lambda x: list(zip(
                    list(map(
                        lambda _: random.uniform(0.0, 1.0),
                        range(8)
                    )),
                    x
                )),
                list(map(
                    lambda x: (x[0][1][0][x[0][0]:] + x[0][1][1][:x[0][0]]) * (1-x[1]) + x[0][1][0][:x[0][0]] + x[0][1][1][x[0][0]:] * (x[1]),
                    list(zip(
                        list(zip(
                            map(lambda _: random.randint(0, 7), range(0, 50)),
                            list(zip(
                                *list(map(
                                    lambda x: x[0][x[1]::2],
                                    list(zip(
                                        [list(map(
                                            lambda x: sorted(x, key=lambda x: x[0])[-1][1],
                                            list(map(
                                                lambda x: list(map(
                                                    lambda _: x[random.randint(0, 49)], 
                                                    range(10)
                                                )),
                                                [list(map(
                                                    lambda x: [
                                                        (8*(8-1))/2 - sum(
                                                            list(map(
                                                                lambda i: int(i%8 != i//8 and x[i//8] == x[i%8]) + 
                                                                    int(i%8 != i//8 and abs(i%8 - i//8) == abs(x[i%8] - x[i//8])),
                                                                range(8*8)
                                                            ))
                                                        ),
                                                        x
                                                    ], 
                                                    val
                                                ))] * 50
                                            ))
                                        ))] * 2,
                                        [0, 1]
                                    ))
                                ))
                            ))
                        ))*2,
                        [0]*50+[1]*50
                    ))
                ))
            ))
        ))
    )

print(gen())
