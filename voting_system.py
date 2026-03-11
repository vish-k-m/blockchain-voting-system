from blockchain import Blockchain

blockchain = Blockchain()

candidates = ["Alice", "Bob", "Charlie"]
voted_users = []

def cast_vote(voter, candidate):

    if voter in voted_users:
        return "You already voted!"

    if candidate not in candidates:
        return "Invalid candidate."

    blockchain.add_vote(voter, candidate)
    voted_users.append(voter)

    return "Vote successfully recorded!"
