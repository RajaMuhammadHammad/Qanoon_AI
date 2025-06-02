from bert_score import score as bert_score

def evaluate_answer(answer, reference_texts):
    if not reference_texts:
        return {"precision": 0, "recall": 0, "f1": 0}
    ref_text = reference_texts[0]['text']
    P, R, F1 = bert_score([answer], [ref_text], lang='en')
    return {
        "precision": round(P.mean().item(), 3),
        "recall": round(R.mean().item(), 3),
        "f1": round(F1.mean().item(), 3)
    }
