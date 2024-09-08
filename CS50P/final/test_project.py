from CS50P.final.project import pull_calc, crimp_calc, hang_calc

def test_pull_calc():
    pull_list = [-1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1, 1.2]
    assert pull_calc(0.1, pull_list) == 2
    assert pull_calc(-1, pull_list) == 0
    assert pull_calc(1.2, pull_list) == 10

def test_crimp_calc():
    crimp_list = [-1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1, 1.2]
    assert crimp_calc(0.1, crimp_list) == 2
    assert crimp_calc(-1, crimp_list) == 0
    assert crimp_calc(1.2, crimp_list) == 10


def test_hang_calc():
    hang_list = [-1, 30, 60, 90, 120, 150, 180, 210, 270, 300, 330]
    assert hang_calc(60, hang_list) == 2
    assert hang_calc(-1, hang_list) == 0
    assert hang_calc(330, hang_list) == 10



