from huffman_coding.HuffmanCoding import HuffmanCoding
from coding.CodingAlgorithms import CodingAlgorithms
from arithmetic_coding.ArithmeticCoding import ArithmeticCoding


def compress(algorithm, input_file_path, output_file_path, secret_file_path):
    if algorithm is CodingAlgorithms.Huffman:
        HuffmanCoding(input_file_path, output_file_path, secret_file_path).compress()
    elif algorithm is CodingAlgorithms.Arithmetic:
        ac = ArithmeticCoding(input_file_path, output_file_path, 10)
        compressed = ac.compress()
        print(compressed)
        decompressed = ac.decompress(compressed)
        print(decompressed)


def decompress(method, input_file_path, output_file_path, secret_file_path=None):
    if method is CodingAlgorithms.Huffman:
        HuffmanCoding(input_file_path, output_file_path, secret_file_path).decompress()
    elif method is CodingAlgorithms.Arithmetic:
        pass
