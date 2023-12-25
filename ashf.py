def shannon_fano(group, start, end, prefix):
    if start >= end:
        return

    if start + 1 == end:
        b[group[start]] = prefix
        return

    total_freq = sum(a[ch] for ch in group[start:end])
    half_freq = total_freq // 2
    current_freq = 0
    split_index = start

    while current_freq + a[group[split_index]] <= half_freq:
        current_freq += a[group[split_index]]
        split_index += 1

    for i in range(start, end):
        if i < split_index:
            b[group[i]] = prefix + "1"
        else:
            b[group[i]] = prefix + "0"

    shannon_fano(group, start, split_index, prefix + "1")
    shannon_fano(group, split_index, end, prefix + "0")


line = input()
a = {}
b = {}
group1 = []
group2 = []

for i in range(len(line)):
    if line[i] not in a:
        a[line[i]] = 1
    else:
        a[line[i]] += 1

shannon_fano(sorted(a.keys()), 0, len(a), "")

print(a)
print(b)