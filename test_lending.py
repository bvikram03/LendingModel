# # Define the inequality function
# def inequality(theta, group):
#     pi = pi_w if group else pi_b
#     compare_value = (1 - pi) / pi
#     return ratio - (compare_value * likelihood_ratio(theta))

# # Generate values for theta and calculate inequality for each
# theta_values = np.linspace(0, 1, 500)
# inequality_values_w = [inequality(theta, True) for theta in theta_values]
# inequality_values_b = [inequality(theta, False) for theta in theta_values]

# # Plot the results
# plt.figure(figsize=(10, 6))
# plt.plot(theta_values, inequality_values_w, label='Group W', color='blue')
# plt.plot(theta_values, inequality_values_b, label='Group B', color='red')
# plt.axhline(0, color='black', linestyle='--')
# plt.xlabel('Theta')
# plt.ylabel('Inequality Value')
# plt.title('Inequality Function vs. Theta')
# plt.legend()
# plt.grid(True)
# plt.show()

# print(inequality_values_w)



# Simulation element
def simulate_borrowers(borrowers, q, u, num_iterations=1000):
    results = []
    for _ in range(num_iterations):
        for borrower in borrowers:
            standard_value = standard(q, u, borrower.pi, ratio)
            assignment_prob = prob_assignment_given_group([borrower], standard_value)
            net_payoff_value = net_payoff(borrower, q, u, cost)
            results.append({
                'group': borrower.group,
                'pi': borrower.pi,
                'theta': borrower.theta,
                'standard': standard_value,
                'assignment_prob': assignment_prob,
                'net_payoff': net_payoff_value
            })
    return results
# Adjusting credit rating
def update_credit_rating(group, increase):
    for borrower in group:
        borrower.pi += increase
        borrower.pi = min(borrower.pi, 1)  # Ensure pi does not exceed 1
# Run the simulation
results = simulate_borrowers(tester_q + tester_u, tester_q, tester_u, num_iterations=1000)
# Print a summary of results
results_df = pd.DataFrame(results)
print(results_df.describe())