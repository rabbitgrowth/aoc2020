bottom_up = Hash.new { |h, k| h[k] = [] }
top_down  = Hash.new { |h, k| h[k] = [] }

File.foreach('input.txt') do |line|
  outer, rhs = line.split(' bags contain ')
  rhs.scan /(\d) (.+?) bag/ do |count, inner|
    bottom_up[inner] << outer
    top_down[outer] << [count.to_i, inner]
  end
end

def possible_outers(bottom_up, bag, seen = [])
  bottom_up[bag].each do |outer|
    if !seen.include?(outer)
      seen << outer
      possible_outers(bottom_up, outer, seen)
    end
  end
  seen.size
end

def total_inners(top_down, bag)
  top_down[bag].sum do |count, inner|
    count * (1 + total_inners(top_down, inner))
  end
end

puts possible_outers(bottom_up, 'shiny gold')
puts total_inners(top_down, 'shiny gold')
