# 🎰 Daily Lotto Prediction Desktop App

A professional desktop application for generating and tracking Daily Lotto number predictions using mathematical formulas based on the Fibonacci sequence and the Golden Ratio (PHI).

## ✨ Features

### 🎯 Prediction Tab
- Input your last draw numbers
- Set custom Lottery Number (LN)
- Generate predictions using 3 advanced mathematical formulas
- View all 9 prediction lines (3 formulas × 3 lines)

### ✅ Verification Tab
- Enter actual winning numbers
- Automatically compare with all generated predictions
- Highlight best matching line
- Track match counts
- Display prize win status

### 📊 History Tab
- Track all your prediction sessions
- View last 10 draws
- See win/loss status for each draw
- Export to CSV for external analysis
- Clear history with one click

### 📈 Analytics Tab
- Win rate percentage
- Total predictions made
- Best match statistics
- Historical trends and metrics

## 🚀 Installation

### Requirements
- Python 3.7+
- PyQt5

### Setup
bash
# Clone the repository
git clone https://github.com/manualpepler-creator/DAILY.git
cd DAILY

# Install dependencies
pip install -r requirements.txt

# Run the application
python main_app.py


## 📖 How to Use

### Step 1: Generate Predictions
1. Open the Predictions tab
2. Enter your last draw numbers (comma-separated, e.g., 6,15,11,33,31)
3. Enter a Lottery Number (default: 23456789) or leave blank
4. Click Generate Predictions
5. View all prediction lines generated from 3 formulas

### Step 2: Verify Results
1. After the actual draw, go to the Verify Results tab
2. Enter the actual winning numbers
3. Click Check Matches
4. View which prediction line matched best
5. See if you won a prize (3+ matches)

### Step 3: Track History
1. Go to the History tab
2. View your last 10 draws with results
3. Export data to CSV for spreadsheet analysis
4. Clear history if needed

### Step 4: Analyze Performance
1. Check the Analytics tab
2. Review win rate and statistics
3. Track your best matches
4. Identify prediction patterns

## 🧮 Mathematical Formulas

The app uses three prediction formulas combining:
- Fibonacci Sequence: Mathematical progression found in nature
- Golden Ratio (PHI): 1.61803398875 - universal aesthetic constant
- Last Draw Numbers: Historical winning numbers
- Custom Lottery Number: User-defined parameter

### Formula 1
result = (FIB[n] × PHI + LN + LastDraw[(n-1) % 5] + n) % 36

### Formula 2
result = (FIB[n] × PHI² + LN + LastDraw[(n-1) % 5] + n) % 36

### Formula 3
result = ((FIB[n] + LN) × PHI + LastDraw[(n-1) % 5] + n) % 36

## 💾 Data Storage

- History: Stored in lotto_history.json in the app directory
- Exports: CSV files saved to your chosen location
- Automatic Backup: History auto-saves after each verification

## 🎯 Understanding Results

### Match Scoring
- 5 matches: Jackpot! 🎉
- 4 matches: Major prize 🎊
- 3 matches: Minor prize 💰
- 2 matches: Small prize possibility 🤞
- 0-1 matches: Better luck next time 📉

## ⚙️ Configuration

### Change Range (1-36)
Edit in prediction_engine.py:
python
self.RANGE = 36  # Change to your lottery's number range


### Change Numbers Per Line (5)
Edit in prediction_engine.py:
python
self.NUMBERS_PER_LINE = 5  # Change to your lottery format


### Change Fibonacci Sequence
Edit in prediction_engine.py:
python
self.FIB = [...]  # Add more Fibonacci numbers if needed


## 📊 Performance Tips

1. Use Historical Data: Better results when using recent winning numbers
2. Experiment with LN: Try different Lottery Numbers to find patterns
3. Track Trends: Use History tab to identify successful formulas
4. Export & Analyze: Export to CSV and analyze in Excel/Sheets

## 🐛 Troubleshooting

### App won't start
bash
pip install --upgrade PyQt5
python main_app.py


### Input validation error
- Ensure 5 numbers separated by commas
- Numbers must be within range 1-36
- Lottery Number must be numeric

### History not saving
- Check file permissions in app directory
- Ensure lotto_history.json is not corrupted
- Delete and restart app to recreate file

## 📝 License

Open source - Feel free to modify and distribute!

## 🤝 Contributing

Got improvements? Fork, modify, and submit a PR!

## 💬 Support

For issues or questions, create a GitHub Issue in this repository.

Good luck with your predictions! 🍀