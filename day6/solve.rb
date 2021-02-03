groups = File.read('input.txt').split("\n\n").map { |group| group.split.map(&:chars) }

puts groups.map { |group| group.reduce(:union).size }.sum
puts groups.map { |group| group.reduce(:intersection).size }.sum
