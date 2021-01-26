FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
ECLS   = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validate1(passport)
  FIELDS.all? { |field| passport.include?(field) }
end

def validate2(passport)
  passport.all? do |key, value|
    case key
    when 'byr'
      value.to_i.between?(1920, 2002)
    when 'iyr'
      value.to_i.between?(2010, 2020)
    when 'eyr'
      value.to_i.between?(2020, 2030)
    when 'hgt'
      validate_hgt(value)
    when 'hcl'
      value =~ /^#[0-9a-f]/
    when 'ecl'
      ECLS.include?(value)
    when 'pid'
      value =~ /^[0-9]{9}$/
    when 'cid'
      true
    end
  end
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
