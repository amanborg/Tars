# template file for tests

from nose.tools import *
from ex47.game import Room

def test_room():
	gold_room = Room("goldroom", "room is full of gold")
	assert_equal(gold_room.name,"goldroom")
	assert_equal(gold_room.paths,{})

def test_path():
    center_rm = Room("Center","Test room in center")
    north_rm = Room("North", "Test room in the north.")
    south_rm = Room("South", "Test room in the south.")
    jackass_mf = Room("Jackass", "No direction")

    center_rm.add_paths({'north': north_rm, 'south': south_rm, 'bingo': jackass_mf})
    jackass_mf.add_paths({'nodir': north_rm,})
    assert_equal(center_rm.go('north'),north_rm)
    assert_equal(center_rm.go('bingo'),jackass_m)
    assert_equal(jackass_mf.go('nodir'),north_rm)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west':west,'down':down})
    west.add_paths({'east':start})
    down.add_paths({'up':start})

    assert_equal(start.go('west'),west)
    assert_equal(start.go('west').go('east'),start)
    assert_equal(start.go('down').go('up'), start)




