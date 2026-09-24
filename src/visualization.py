# visualization.py

import matplotlib.pyplot as plt
import seaborn as sns


class EmployeeVisualizer:

    def __init__(self, data):
        self.data = data

    def plot_average_salary_by_position_year(self):
        avg_salary = (
            self.data
            .groupby(["start_year", "position"])["salary"]
            .mean()
            .reset_index()
        )

        salary_pivot = avg_salary.pivot(
            index="start_year",
            columns="position",
            values="salary"
        )

        salary_pivot.plot(
            kind="bar",
            figsize=(14, 7)
        )

        plt.title("Average Salary by Position and Start Year")
        plt.xlabel("Start Year")
        plt.ylabel("Average Salary ($)")
        plt.xticks(rotation=45)
        plt.legend(
            title="Position",
            bbox_to_anchor=(1.05, 1),
            loc="upper left"
        )
        plt.tight_layout()
        plt.show()
        
    def plot_salary_heatmap(self):

        salary_heatmap = self.data.pivot_table(
            values="salary",
            index="department_name",
            columns="position",
            aggfunc="mean"
        )

        plt.figure(figsize=(14, 6))

        sns.heatmap(
            salary_heatmap,
            annot=True,
            fmt=".0f",
            cmap="YlGnBu"
        )

        plt.title("Average Salary by Department and Position")
        plt.xlabel("Position")
        plt.ylabel("Department")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        plt.show()