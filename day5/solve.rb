seats = File.read('input.txt').tr('FBLR', '0101').lines.map { |line| line.to_i(2) }

puts seats.max
puts seats.sort.each_cons(2).find { |a, b| b - a == 2 }.first + 1
