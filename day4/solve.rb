FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

passports = File.read('input.txt').split("\n\n").map do |passport|
  passport.split.map { |field| field.split(':') }.to_h
end

valid_count = passports.count do |passport|
  FIELDS.all? { |field| passport.include?(field) }
end

puts valid_count
