class Result:
    def __init__(self, input_file_size, output_file_size, time):
        self.input_file_size = input_file_size
        self.output_file_size = output_file_size
        self.time = time

    def __str__(self):
        return "Ievādes faila izmērs = {input_file_size} bytes\n" \
               "Izvādes faila izmērs = {output_file_size} bytes\n" \
               "Paterētais laiks = {time} ms".format(input_file_size=self.input_file_size,
                                                     output_file_size=self.output_file_size,
                                                     time=round(self.time * 1000, 3))
