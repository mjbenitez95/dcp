
NUMS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def run_length_encode(str)
  encoded = ''
  current_character = ''
  count = 0
  
  str.each_char do |c|
    if c != current_character 
      encoded.concat(count.to_s + current_character) if count != 0
      current_character = c
      count = 1
    else
      count += 1
    end
  end

  encoded.concat(count.to_s + current_character) if count != 0
end

def run_length_decode(str)
  decoded = ''
  count, index = 0, 0
  str_len = str.length

  while index < str.length
    if NUMS.include?(str[index])
      count = str[index].to_i
    else
      decoded += (str[index] * count)
    end
    index += 1
  end

  decoded
end

def main
  encoded = run_length_encode("AAAABBBCCDAA")
  decoded = run_length_decode("4A3B2C1D2A")
  puts (encoded == '4A3B2C1D2A')
  puts (decoded == 'AAAABBBCCDAA')
  puts (run_length_decode(run_length_encode('AAAABBBCCDAA')) == 'AAAABBBCCDAA')
end

main()
