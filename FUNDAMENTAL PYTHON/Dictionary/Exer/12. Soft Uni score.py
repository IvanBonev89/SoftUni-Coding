submissions_dict = {}
results_dict = {}

while True:
    line = input()
    if line == "exam finished":
        break
    if "banned" in line:
        name, status = line.split("-")
        results_dict.pop(name)
        continue
    else:

        name, language, score = line.split("-")
        if name not in results_dict:
            results_dict[name] = []

        if language not in submissions_dict:
            submissions_dict[language] = 0

        if line.endswith("banned"):
            results_dict.pop(name)
            continue

        submissions_dict[language] += 1

        if not results_dict[name]:
            results_dict[name].append(int(score))
        else:
            if int(score) > max(results_dict[name]):
                results_dict[name] = [score]

print("Results:")
for name, scores in results_dict.items():
    best_score = max(scores)
    print(f"{name} | {best_score}")

print("Submissions:")
for language, count in submissions_dict.items():
    print(f"{language} - {count}")
