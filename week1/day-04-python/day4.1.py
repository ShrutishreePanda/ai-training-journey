class DataProcessing:
    def __init__(self, data):
        self.data = data

    def get_max(self):
        return max(self.data)

    def get_min(self):
        return min(self.data)

    def get_average(self):
        return sum(self.data) / len(self.data)

data = [10, 20, 30, 40]
process = DataProcessing(data)

print("Max:", process.get_max())
print("Min:", process.get_min())
print("Average:", process.get_average())