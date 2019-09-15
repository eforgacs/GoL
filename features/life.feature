Feature: basic life
  # For a space that is 'populated':
    # Each cell with one or no neighbors dies, as if by solitude.
    # Each cell with four or more neighbors dies, as if by overpopulation.
    # Each cell with two or three neighbors survives.
  # For a space that is 'empty' or 'unpopulated'
    # Each cell with three neighbors becomes populated.

  Scenario: cell death
    Given a 3x3 board
      And cell 1,1 is alive
      And life board instantiated
     When cycled
      And board retrieved
     Then cell 1,1 is dead