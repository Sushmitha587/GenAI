def cancel_user_subscription(client, user_email: str):
    # 1) Find user by email
    users = client.get("/users", params={"email": user_email})
    if not users:
        raise ValueError("User not found")
    user_id = users[0]["id"]

    # 2) Get active subscription
    sub = client.get(f"/users/{user_id}/subscriptions/active")
    sub_id = sub["id"]

    # 3) Cancel subscription
    result = client.post(f"/subscriptions/{sub_id}/cancel", json={})
    return result