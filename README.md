# python-sudoku-generator
This is a small project I took on to learn and get more accustomed with Python

# How it works
<ol>
  <li>Generate empty sudoku board</li>
  <li>"Solve" the empty sudoku board using a custom solver with randomised values</li>
  <li>Remove some tiles from the filled sudoku board</li>
  <li>Attempt to solve the sudoku board again and if it's solvable print it else remove another set of tiles from the filled sudoku board and try again</li>
</ol>

# Example board
```
+-------------+-------------+-------------+
|  5       4  |             |  2   3   7  |
|          1  |  7       3  |      4      |
|  6       7  |  8   2   4  |  9   1      |
+-------------+-------------+-------------+
|      9   5  |  4          |  3   6   1  |
|  7   4      |             |      2   9  |
|  3          |  6       8  |  5          |
+-------------+-------------+-------------+
|  2          |  5       9  |      8   6  |
|  4   6      |  2       7  |      5   3  |
|             |      4   6  |          2  |
+-------------+-------------+-------------+
```
