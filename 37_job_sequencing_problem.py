class Solution:
    def jobSequencing(self, deadline, profit):
        # Create a list of jobs with their deadlines and profits
        jobs = list(zip(deadline, profit))
        # Sort jobs based on profit in descending order
        jobs.sort(key=lambda x: x[1], reverse=True)

        # Find the maximum deadline to determine the size of the schedule
        max_deadline = max(deadline)
        schedule = [False] * (max_deadline + 1)  # +1 to accommodate 1-based indexing

        total_profit = 0
        job_count = 0
        for d, p in jobs:
            # Try to find a free slot for this job (starting from its deadline)
            for j in range(d, 0, -1):
                if schedule[j] is False:  # If the slot is free
                    schedule[j] = True  # Assign the job to this slot
                    total_profit += p      # Add profit
                    job_count += 1         # Increment the count of jobs done
                    break  # Move to the next job

        return job_count, total_profit


# Example usage:
solution = Solution()
job_count, total_profit = solution.jobSequencing([4, 1, 1, 1],  [20, 10, 40, 30])
print(f"Number of jobs done: {job_count}")
print(f"Total profit: {total_profit}")

# Example usage:
job_count, total_profit = solution.jobSequencing([2, 1, 2, 1, 1], [100, 19, 27, 25, 15])
print(f"Number of jobs done: {job_count}")
print(f"Total profit: {total_profit}")

# Example usage:
job_count, total_profit = solution.jobSequencing([3, 1, 2, 2], [50, 10, 20, 30])
print(f"Number of jobs done: {job_count}")
print(f"Total profit: {total_profit}")