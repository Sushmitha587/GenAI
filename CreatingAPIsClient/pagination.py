import requests
import time

# --------------------------------------
# 1) RETRY WITH EXPONENTIAL BACKOFF
# --------------------------------------

def get_with_retry(url, max_retries=3):
    for attempt in range(max_retries):

        try:
            print(f"Trying: {url} | Attempt {attempt + 1}")
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            print("✅ Success\n")
            return response

        except requests.exceptions.RequestException as e:
            wait = 2 ** attempt   # 1, 2, 4 seconds
            print(f"❌ Failed: {e}")

            if attempt == max_retries - 1:
                raise Exception("Max retries reached")

            print(f"⏳ Waiting {wait} seconds before retry...\n")
            time.sleep(wait)


# --------------------------------------
# 2) PAGINATION (GitHub Issues)
# --------------------------------------

def get_all_issues(owner, repo):
    page = 1
    per_page = 5
    all_issues = []

    while True:
        print(f"\nFetching page {page}")

        url = f"https://api.github.com/repos/{owner}/{repo}/issues"
        params = {"page": page, "per_page": per_page}

        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()

        issues = response.json()

        if not issues:
            print("✅ No more pages\n")
            break

        print(f"Page {page} → {len(issues)} issues")

        for issue in issues:
            print("•", issue["title"])

        all_issues.extend(issues)
        page += 1

    return all_issues 


# --------------------------------------
# 3) MULTI-STEP WORKFLOW
# Using dummy API: jsonplaceholder
# --------------------------------------

def multi_step_example(user_id):

    print("\nSTEP 1: Getting user info")
    user = get_with_retry(f"https://jsonplaceholder.typicode.com/users/{user_id}").json()
    print("User:", user["name"])

    print("\nSTEP 2: Getting posts for the user")
    posts = get_with_retry(f"https://jsonplaceholder.typicode.com/posts?userId={user_id}").json()
    print("Posts found:", len(posts))

    post_id = posts[0]["id"]

    print("\nSTEP 3: Getting comments for first post")
    comments = get_with_retry(f"https://jsonplaceholder.typicode.com/comments?postId={post_id}").json()
    print("Comments found:", len(comments))

    result = {
        "user": user["name"],
        "total_posts": len(posts),
        "total_comments_for_first_post": len(comments)
    }

    return result


# --------------------------------------
# MAIN - Runs All 3
# --------------------------------------

if __name__ == "__main__":

    print("\n========== PAGINATION ==========")
    all_issues = get_all_issues("octocat", "Spoon-Knife")
    print(f"\n✅ TOTAL ISSUES COLLECTED: {len(all_issues)}")


    print("\n========== RETRY TEST ==========")
    r = get_with_retry("https://api.github.com/users/octocat")
    print("User:", r.json()["login"])
    print("Public repos:", r.json()["public_repos"])


    print("\n========== MULTI-STEP WORKFLOW ==========")
    result = multi_step_example(1)
    print("\nFINAL RESULT:", result)
