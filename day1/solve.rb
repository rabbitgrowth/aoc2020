File.open('input.txt') do |file|
  nums = file.readlines.map(&:to_i)
  [2, 3].each do |r|
    puts nums.combination(r).find { |nums| nums.reduce(:+) == 2020 }.reduce(:*)
  end
end
