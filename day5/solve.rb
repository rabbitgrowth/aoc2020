seats = File.foreach('input.txt').map do |seat|
  seat.tr('FBLR', '0101').to_i(2)
end

puts seats.max
puts seats.sort.each_cons(2).find { |a, b| b - a == 2 }.first + 1
