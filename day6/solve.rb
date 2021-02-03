groups = File.read('input.txt').split("\n\n").map do |group|
  group.split.map(&:chars)
end

[:union, :intersection].each do |operation|
  puts groups.map { |group| group.reduce(operation).size }.sum
end
