# Guttr

A Gettr client library written in Python.

I rushed to get this out so it's a bit janky. Open an issue if something is broken or missing.

## Getting Started

Authenticate to Gettr and export the `x-app-auth` token and your user name as environment variables.
You can find these values in the HTTP request header of any call to an `api.gettr.com` endpoint.
```shell
export user="foo"
export token="ey..."
```

### Example
#### Retrive users posts
```python
from guttr import *

# Instantiate the API endpoint class
p = Post()

# Retrieve the most recent 20 posts
p.get_user_posts(user_id='newsmax', maximum=20, direction="rev")

# Retrieve the least recent 20 posts
p.get_user_posts(user_id='newsmax', maximum=20, direction="fwd")

# Retrieve all posts
p.get_user_posts(user_id='newsmax', direction="rev", follow=True)
```

#### Content recommendation
```python
from guttr import *

# Instantiate the API endpoint class
p = Suggest()

# Retrieve the top 10 suggestions
p.suggest_hashtag(maximum=10)
```

#### Search post content
```python
from guttr import *

# Instantiate the API endpoint class
p = Post()

# Retrieve the top 10 suggestions
p.search_posts(query="how to insurrection", maximum=10)
```

## API Methods

### Alerts

```python
p = Alert()
p.get_alert_count()
p.get_alerts()
p.get_alert_status()
```

### Comments

```python
p = Comment()
p.get_post_comments()
p.get_comment_comments()
```

### Feed

```python
FIX ME
```

### Follow

```python
p = Follow()
p.get_follow_status()
p.get_follows()
p.get_followers()
p.unfollow()
p.follow()
```

### Like

```python
p = Like()
p.like_post()
p.unlike_post()
p.like_comment()
p.unlike_comment()
p.get_post_likes_by_user
```

### Post

```python
p = Post()
p.get_post()
p.get_post_comments()
p.get_post_comments()
p.search_posts()
```

### Watch

```python
FIX ME
```

### User

```python
p = User()
p.get_mutes()
p.get_blocks()
p.mute()
p.unmute()
p.block()
p.unblock()
p.does_user_exist()
p.does_email_exist()
```

### Suggest

```python
p = Suggest()
p.suggest_hashtag()
p.suggest_user()
```