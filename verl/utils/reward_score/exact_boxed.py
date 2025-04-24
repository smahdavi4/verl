from typing import Optional
from .math_dapo import last_boxed_only_string, remove_boxed

def compute_score(solution_str: str,
                 ground_truth: str) -> dict:
    """Compute reward score based on exact match of boxed answers.
    
    Args:
        solution_str: The solution string
        ground_truth: The ground truth answer
        strict_box_verify: Not used, kept for API compatibility
        pause_tokens_index: Optional list of pause token indices
        
    Returns:
        Dictionary containing score (1.0 for match, 0.0 otherwise), accuracy and prediction
    """
    # Extract boxed answer from solution
    boxed_pred = last_boxed_only_string(solution_str)
    pred = remove_boxed(boxed_pred) if boxed_pred is not None else None
    
    # Check exact match
    correct = (pred == ground_truth)
    
    return {
        "score": float(correct),
        "acc": correct,
        "pred": pred if pred is not None else "Error-NoBoxed",
    }