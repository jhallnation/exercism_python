def latest(scores):
    latest_score = scores[-1]
    return latest_score


def personal_best(scores):
    highest_score = sorted(scores)[-1]
    return highest_score


def personal_top_three(scores):
    top_three_scores = sorted(scores, reverse=True)[:3]
    return top_three_scores