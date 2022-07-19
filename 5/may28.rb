OPENINGS = ['[', '(', '{']
CLOSINGS = [']', ')', '}']

MAPPINGS = {
  "]" => "[",
  ")" => "(",
  "}" => "{",
}

def balanced(str)
  stack = []
  str.each_char do |c|
    if OPENINGS.include?(c)
      stack.append(c)
    elsif CLOSINGS.include?(c)
      if MAPPINGS[c] == stack[-1]
        stack.pop
      else
        return false
      end
    end
  end

  stack.empty?
end
  

def main()
  puts(balanced('[](){}') == true)
  puts(balanced('[][][]}]') == false)
  puts(balanced('[{}]({{[]}})') == true)
  puts(balanced('[{]}({{[]}})') == false)
end

main()
