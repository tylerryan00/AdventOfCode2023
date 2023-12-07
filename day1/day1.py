def pt1(calibration_document):
    answer = 0
    for line in calibration_document:
        numbers = [int(char) for char in line if char.isdigit()]
        calibration_value = int(''.join(map(str, [numbers[0], numbers[-1]])))
        answer += calibration_value
    return answer

# def pt2(calibration_document):
#     approved_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     for line in calibration_document:
#         split_string = line.split(approved_list)
#         print(split_string)
#     #     numbers = [int(char) for char in line if char.isdigit() or char in a]
#     #     calibration_value = int(''.join(map(str, [numbers[0], numbers[-1]])))
#     #     answer += calibration_value
#     # return answer

def main():
    with open ('day1_input.txt', 'r') as file:
        calibration_document = [line.strip() for line in file.readlines()]
    
    print(f'Part One: {pt1(calibration_document)}')
    # print(f'Part Two: {pt2(calibration_document)}')
    


if __name__ == '__main__':
    main()