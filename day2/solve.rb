PATTERN = /(\d+)-(\d+) (.): (.+)/

count1 = 0
count2 = 0

File.open('input.txt') do |file|
  file.each_line do |line|
    x, y, letter, password = PATTERN.match(line).captures
    x = x.to_i
    y = y.to_i
    if password.count(letter).between?(x, y)
      count1 += 1
    end
    if [password[x-1], password[y-1]].count(letter) == 1
      count2 += 1
    end
  end
end

puts count1
puts count2
