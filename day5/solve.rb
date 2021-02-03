seats = File.read('input.txt').tr('FBLR', '0101').lines.map { |line| line.to_i(2) }

puts seats.max
puts (seats.min..seats.max).to_a - seats
