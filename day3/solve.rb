MAP = File.foreach('input.txt').map(&:chomp)

WIDTH  = MAP[0].size
HEIGHT = MAP.size

def count_trees(dx, dy)
  trees = 0
  x = 0
  y = 0
  loop do
    x += dx
    y += dy
    break if y >= HEIGHT
    if MAP[y][x % WIDTH] == '#'
      trees += 1
    end
  end
  trees
end

puts count_trees(3, 1)

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
puts slopes.map { |slope| count_trees(*slope) }.reduce(:*)
