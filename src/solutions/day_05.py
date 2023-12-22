import re
from src.utils import get_whole_file

resource = "day_05.txt"
content = get_whole_file(resource)


def extract_data_from_file():
    sections = content.split('\n\n')

    transformed_maps = []
    for section in sections[1:]:
        title, data = section.split(':\n')
        transformed_maps.append([(int(entry[1]), int(entry[1]) + int(entry[2]) - 1, int(entry[0]))
                                 for entry in (line.split() for line in data.split('\n'))])

    return sections[0].split(': ')[1].split(), transformed_maps


seeds, maps = extract_data_from_file()
seed_ranges = [(int(start), int(start) + int(end) - 1) for start, end in re.findall(r"(\d+) (\d+)", content.splitlines()[0])]


def convert_to_location(number):
    for values in maps:
        for value in values:
            source = value[0]
            destination = value[2]

            if source < number < value[1]:
                number = destination + (number - source)
                break

    return number


def part1():
    lowest = None
    for seed in seeds:
        location = convert_to_location(int(seed))
        if lowest is None or location < lowest:
            lowest = location

    print(lowest)


def process_seed_ranges():
    for current_map in maps:
        new_converted_seeds = []
        for i, seed_range in enumerate(seed_ranges):
            for start, end, to in current_map:
                conversion = to - start

                if seed_range[0] >= start and seed_range[1] <= end:
                    seed_ranges[i] = (seed_range[0] + conversion, seed_range[1] + conversion)
                    break
                elif seed_range[0] < start <= seed_range[1]:
                    if seed_range[1] <= end:
                        seed_ranges[i] = (seed_range[0], start - 1)
                        new_converted_seeds.append((start + conversion, seed_range[1] + conversion))
                    else:
                        seed_ranges[i] = (seed_range[0], start - 1)
                        new_converted_seeds.append((start + conversion, end + conversion))
                        seed_ranges.insert(i + 1, (end + 1, seed_range[1]))
                elif start <= seed_range[0] <= end:
                    new_converted_seeds.append((seed_range[0] + conversion, end + conversion))
                    seed_ranges[i] = (end + 1, seed_range[1])

                seed_range = seed_ranges[i]

        seed_ranges.extend(new_converted_seeds)

    return min([x[0] for x in seed_ranges])


def part2():
    print(process_seed_ranges())


if __name__ == '__main__':
    part1()
    part2()
