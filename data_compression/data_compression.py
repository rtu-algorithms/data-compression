from huffman_coding.HuffmanCoding import HuffmanCoding


def huffman_coding():
    path = "files/input.txt"
    h = HuffmanCoding(path)
    output_path = h.compress()
    h.decompress(output_path)
