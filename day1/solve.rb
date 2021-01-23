nums = File.foreach('input.txt').map(&:to_i)

[2, 3].each do |r|
  puts nums.combination(r).find { |nums| nums.sum == 2020 }.reduce(:*)
end
