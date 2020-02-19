from huffman_coding.HuffmanCoding import HuffmanCoding
from coding.CodingAlgorithms import CodingAlgorithms


def compress(algorithm, input_file_path, output_file_path, secret_file_path):
    if algorithm is CodingAlgorithms.Huffman:
        HuffmanCoding(input_file_path, output_file_path, secret_file_path).compress()
    elif algorithm is CodingAlgorithms.Arithmetic:
        pass


def decompress(method, input_file_path, output_file_path, secret_file_path=None):
    if method is CodingAlgorithms.Huffman:
        HuffmanCoding(input_file_path, output_file_path, secret_file_path).decompress()
    elif method is CodingAlgorithms.Arithmetic:
        pass
