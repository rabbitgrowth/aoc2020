groups = File.read('input.txt').split("\n\n").map { |group| group.split.map(&:chars) }

puts groups.map { |group| group.reduce(:|).size }.sum
puts groups.map { |group| group.reduce(:&).size }.sum
