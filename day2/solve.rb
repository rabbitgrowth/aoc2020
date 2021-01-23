PATTERN = /(\d+)-(\d+) (.): (.+)/

lines = File.foreach('input.txt').map do |line|
  x, y, letter, password = PATTERN.match(line).captures
  [x.to_i, y.to_i, letter, password]
end

count1 = lines.count do |min, max, letter, password|
  password.count(letter).between?(min, max)
end

count2 = lines.count do |i, j, letter, password|
  [password[i-1], password[j-1]].count(letter) == 1
end

puts count1
puts count2
