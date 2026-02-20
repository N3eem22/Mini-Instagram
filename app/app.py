from fastapi import FastAPI , HTTPException

app = FastAPI()

text_posts = {1 :{"title": "First Post", "content": "This is the content of the first post."},
              2 :{"title": "Second Post", "content": "This is the content of the second post."}
            }

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit is not None:
        return list(text_posts.items())[:limit]
    return text_posts

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    post = text_posts.get(post_id)
    if post:
        return post
    else:
        raise HTTPException(status_code=404, detail="Post not found")