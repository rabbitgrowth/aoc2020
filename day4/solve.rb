FIELDS = %w(byr iyr eyr hgt hcl ecl pid)
ECLS   = %w(amb blu brn gry grn hzl oth)

def validate1(passport)
  (FIELDS - passport.keys).empty?
end

def validate2(passport)
  passport['byr'].to_i.between?(1920, 2002) &&
  passport['iyr'].to_i.between?(2010, 2020) &&
  passport['eyr'].to_i.between?(2020, 2030) &&
  validate_hgt(passport['hgt'])             &&
  passport['hcl'] =~ /^#[0-9a-f]/           &&
  ECLS.include?(passport['ecl'])            &&
  passport['pid'] =~ /^[0-9]{9}$/
end

def validate_hgt(value)
  match = /^(\d+)(cm|in)$/.match(value)
  return false unless match
  num, unit = match.captures
  num = num.to_i
  case unit
  when 'cm'
    num.between?(150, 193)
  when 'in'
    num.between?(59, 76)
  end
end

passports = File.read('input.txt').split("\n\n").map do |passport|
  passport.split.map { |field| field.split(':') }.to_h
end
passports = passports.select { |passport| validate1(passport) }
puts passports.size
puts passports.count { |passport| validate2(passport) }
