from collections import Counter
from .utils import cumulative_freq


class ArithmeticCoding:
    def __init__(self, input_file_path, output_file_path, radix=10):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.radix = radix
        self.power = None
        self.freq = None

    def compress(self):
        print(">>> ArithmeticCoding:compress - START")
        with open(self.input_file_path, 'r+') as input_file, \
                open(self.output_file_path, 'wb') as output_file:
            input_str = input_file.read().rstrip()

            byte_str = bytes(input_str, 'utf-8')
            # The frequency characters
            freq = Counter(byte_str)

            # The cumulative frequency table
            cf = cumulative_freq(freq)

            # Base
            base = len(byte_str)

            # Lower bound
            lower = 0

            # Product of all frequencies
            pf = 1

            # Each term is multiplied by the product of the
            # frequencies of all previously occurring symbols
            for b in byte_str:
                lower = lower * base + cf[b] * pf
                pf *= freq[b]

            # Upper bound
            upper = lower + pf

            power = 0
            while True:
                pf //= self.radix
                if pf == 0: break
                power += 1

            enc = (upper - 1) // self.radix ** power
            self.power = power
            self.freq = freq

            print("%-25s=> %19s * %d^%s" % (input_str, enc, self.radix, self.power))
            to_output_file = enc * pow(self.radix, self.power)
            output_file.write(bytes(str(to_output_file).encode()))
        print(">>> ArithmeticCoding:compress - FINISH")
        return enc

    def decompress(self, enc):
        # Multiply enc by radix^pow
        enc *= self.radix ** self.power;

        # Base
        base = sum(self.freq.values())

        # Create the cumulative frequency table
        cf = cumulative_freq(self.freq)

        # Create the dictionary
        dict = {}
        for k, v in cf.items():
            dict[v] = k

        # Fill the gaps in the dictionary
        lchar = None
        for i in range(base):
            if i in dict:
                lchar = dict[i]
            elif lchar is not None:
                dict[i] = lchar

        # Decode the input number
        decoded = bytearray()
        for i in range(base - 1, -1, -1):
            power = base ** i
            div = enc // power

            c = dict[div]
            fv = self.freq[c]
            cv = cf[c]

            rem = (enc - power * cv) // fv

            enc = rem
            decoded.append(c)

        # Return the decoded output
        return bytes(decoded).decode("utf-8")
