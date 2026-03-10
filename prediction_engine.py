class LottoPredictionEngine:
    def __init__(self, previous_draws):
        self.previous_draws = previous_draws
        self.prediction = []

    def calculate_frequencies(self):
        frequency = {}  
        for draw in self.previous_draws:
            for number in draw:
                if number in frequency:
                    frequency[number] += 1
                else:
                    frequency[number] = 1
        return frequency

    def predict_next_draw(self):
        frequencies = self.calculate_frequencies()
        self.prediction = sorted(frequencies, key=frequencies.get, reverse=True)
        return self.prediction[:6]  # returns top 6 predicted numbers

    def run_prediction(self):
        predicted_numbers = self.predict_next_draw()
        return predicted_numbers

# Example of using the class
previous_draws = [
    [1, 3, 5, 7, 9, 11],
    [2, 3, 4, 6, 8, 10],
    [1, 2, 3, 4, 5, 6],
    [1, 4, 5, 6, 7, 8],
]

engine = LottoPredictionEngine(previous_draws)
print(engine.run_prediction())
