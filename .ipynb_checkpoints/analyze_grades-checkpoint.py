import matplotlib.pyplot as plt
import pandas as pd
# Load the CSV file into a Pandas DataFrame
df = pd.read_csv("Grades_Short.csv")

# Calculate the average of several columns
df['Average'] = df[['Quiz_1', 'Quiz_2', 'Mid_Term_Exam', 'Final_Exam']].mean(axis=1)

# Define a function for letter grades
def calculate_letter_grade(final_grade):
    if final_grade > 90:
        return "A+"
    elif final_grade > 80:
        return "A"
    elif final_grade > 70:
        return "B"
    elif final_grade > 60:
        return "C"
    elif final_grade > 55:
        return "D"
    else:
        return "F"

# Apply the letter grade function to generate a new column
df['Letter Grade'] = df['Average'].apply(calculate_letter_grade)

plt.hist(df['Average'], bins=10, edgecolor='k')
plt.xlabel('Average Grade')
plt.ylabel('Number of Students')
plt.title('Distribution of Average Grades')
plt.show()
plt.savefig('grade_distribution.png', dpi=300, bbox_inches='tight')

# Save the modified data as a new CSV file
df.to_csv("Grades_Modified.csv", index=False)