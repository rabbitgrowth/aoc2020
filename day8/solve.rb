require 'set'

program = File.foreach('input.txt').map do |line|
  operation, argument = line.split
  [operation, argument.to_i]
end

def run(program)
  pointer     = 0
  accumulator = 0
  seen        = Set.new

  loop do
    seen << pointer
    operation, argument = program[pointer]
    case operation
    when 'acc'
      accumulator += argument
      pointer += 1
    when 'jmp'
      pointer += argument
    when 'nop'
      pointer += 1
    end
    return [accumulator, 1] if seen.include? pointer
    return [accumulator, 0] if pointer == program.size
  end
end

puts run(program).first

program.each_with_index do |(operation, argument), i|
  copy = program.dup
  case operation
  when 'acc'
    next
  when 'jmp'
    copy[i] = ['nop', argument]
  when 'nop'
    copy[i] = ['jmp', argument]
  end
  accumulator, exit_status = run(copy)
  if exit_status == 0
    puts accumulator
    break
  end
end
