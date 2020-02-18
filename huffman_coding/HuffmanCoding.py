import heapq
import os
from .HeapNode import HeapNode
from .utils import make_frequency_dict, pad_encoded_text, get_byte_array, remove_padding


class HuffmanCoding:
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse = {}

    def make_heap(self, frequency):
        for key in frequency:
            heapq.heappush(self.heap, HeapNode(key, frequency[key]))

    def merge_nodes(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged_node = HeapNode(None, node1.frequency + node2.frequency)
            merged_node.left = node1
            merged_node.right = node2

            heapq.heappush(self.heap, merged_node)

    def make_codes_helper(self, root, current):
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current
            self.reverse[current] = root.char
            return

        self.make_codes_helper(root.left, current + "0")
        self.make_codes_helper(root.right, current + "1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    def get_encoded_text(self, text: str) -> str:
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text

    def compress(self) -> str:
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + ".bin"

        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()

            frequency = make_frequency_dict(text)
            self.make_heap(frequency)
            self.merge_nodes()
            self.make_codes()

            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = pad_encoded_text(encoded_text)

            b = get_byte_array(padded_encoded_text)
            output.write(bytes(b))

        return output_path

    def decode_text(self, encoded_text: str) -> str:
        print(self.reverse)
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse:
                decoded_text += self.reverse[current_code]
                current_code = ""

        return decoded_text

    def decompress(self, input_path: str, secret_path: str) -> str:
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"

        with open(input_path, 'rb') as input_file, open(output_path, 'w') as output_file:
            bit_string = ""

            byte = input_file.read(1)
            while len(byte) > 0:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = input_file.read(1)

            encoded_text = remove_padding(bit_string)

            decompressed_text = self.decode_text(encoded_text)

            output_file.write(decompressed_text)

        return output_path
