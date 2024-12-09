input_file = "day09/input.txt"
sample_file = "day09/sample.txt"


def defrag_and_checksum_part1(data_file) -> int:
    result = 0
    diskmap = [int(s) for s in open(data_file).read().strip()]
    disk = []

    for idx, block in enumerate(diskmap):
        if (idx % 2) == 0:
            for i in range(block):
                disk.append(str(int(idx/2)))
        else:
            for i in range(block):
                disk.append('.')
    print('Diskmap:\n{}'.format(diskmap))
    print('Disk:\n{}'.format(''.join(disk)))

    return result

if __name__ == "__main__":
    print('────────────────────────────────\nPart 1 sample: {}'.format(defrag_and_checksum_part1(sample_file)))
    # print('────────────────────────────────\nPart 1 input : {}'.format(defrag_and_checksum_part1(input_file)))
