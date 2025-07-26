
def analyze_streaks(results):
    patterns = []
    if not results:
        return patterns

    count = 1
    for i in range(1, len(results)):
        if results[i] == results[i-1]:
            count += 1
        else:
            patterns.append((results[i-1], count))
            count = 1
    patterns.append((results[-1], count))
    return patterns

def summarize_patterns(patterns):
    return {
        'Cầu bệt dài (>=4)': sum(1 for p in patterns if p[1] >= 4),
        'Cầu nhảy (1)': sum(1 for p in patterns if p[1] == 1),
        'Cầu hai dây (2)': sum(1 for p in patterns if p[1] == 2)
    }

def predict_next_move(results):
    if len(results) < 3:
        return "Không đủ dữ liệu"

    if results[-1] == results[-2] == results[-3]:
        return f"Có thể tiếp tục cầu bệt: {results[-1]}"
    elif results[-1] != results[-2] and results[-2] != results[-3]:
        return "Cầu nhảy – có thể đảo chiều"
    else:
        return f"Xu hướng nghiêng về: {results[-1]}"
