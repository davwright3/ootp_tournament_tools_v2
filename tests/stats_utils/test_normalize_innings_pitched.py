import utils.stats_utils.normalize_innings_pitched as mod

def test_normalize_innings_pitched():
    ipc = mod.normalize_innings_pitched(2.1)

    assert ipc == 2.3333333333333335