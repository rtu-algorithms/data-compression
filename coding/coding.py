from huffman_coding.HuffmanCoding import HuffmanCoding
from coding.CodingAlgorithms import CodingAlgorithms


def compress(method):
    if method is CodingAlgorithms.Huffman:
        pass
    elif method is CodingAlgorithms.Arithmetic:
        pass


def decompress(method):
    if method is CodingAlgorithms.Huffman:
        pass
    elif method is CodingAlgorithms.Arithmetic:
        pass


def huffman_coding():
    path = "files/input.txt"
    h = HuffmanCoding(path)
    output_path = h.compress()
    h.decompress(output_path)
