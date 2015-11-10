def range_overlap(ranges):
    '''Return common overlap among a set of [low, high] ranges.'''
    lowest = 0.0
    highest = 100.0
    for (low, high) in ranges:
      lowest = max(lowest, low)
      highest = min(highest, high)
    if highest < lowest:
      return None
    else:
      return (lowest, highest)
def test_range_overlap():
    assert range_overlap([(0.0, 1.0), (5.0,6.0)]) == None, 'Test should return none'
    print 'test one'
    assert range_overlap([(0.0, 1.0)]) == (0.0, 1.0), 'Test should return (0.0,  1.0)'
    print 'test two'
    assert range_overlap([(2.0, 3.0), (2.0, 4.0)]) == None, 'Test should return a value'
    print 'test three'
test_range_overlap()
