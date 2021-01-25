MAP = File.foreach('input.txt').map(&:chomp)

WIDTH  = MAP[0].size
HEIGHT = MAP.size

def count_trees(dx, dy)
  (0...HEIGHT).step(dy).each_with_index.count do |y, i|
    x = (dx * i) % WIDTH
    MAP[y][x] == '#'
  end
end

puts count_trees(3, 1)

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
puts slopes.map { |slope| count_trees(*slope) }.reduce(:*)
