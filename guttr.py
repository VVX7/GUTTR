from utilities.wrappers import paginate
from utilities.client import client

class _Guttr:
    """
    Base class for Gettr API endpoints.
    """

    def __init__(self):
        self.parler_url = "https://api.gettr.com"
        self.session = client()

    def _get_request(self, route, **kwargs):
        """
        GET request class.
        :param method: http method
        :param route: tapi route
        :param kwargs:
        :return: requests.Reponse
        """
        url = self.parler_url + route
        response = self.session.get(url=url, **kwargs)
        return response

    def _post_request(self, route, **kwargs):
        """
        POST request class.
        :param method: http method
        :param route: tapi route
        :param kwargs:
        :return: requests.Reponse
        """
        url = self.parler_url + route
        response = self.session.post(url=url, **kwargs)
        return response

    def _patch_request(self, route, **kwargs):
        """
        PATCH request class.
        :param method: http method
        :param route: tapi route
        :param kwargs:
        :return: requests.Reponse
        """
        url = self.parler_url + route
        response = self.session.patch(url=url, **kwargs)
        return response

    def _delete_request(self, route, **kwargs):
        """
        PATCH request class.
        :param method: http method
        :param route: tapi route
        :param kwargs:
        :return: requests.Reponse
        """
        url = self.parler_url + route
        response = self.session.delete(url=url, **kwargs)
        return response


class Alert(_Guttr):
    """
    Alerts
    """

    def __init__(self):
        _Guttr.__init__(self)

    def get_alert_count(self, user_id=None, field=None, request_params=None, **kwargs):
        """
        Returns alert count of field.
        :param user_id: user ID
        :param field: notification field
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/count/alerts/{field}"
        return self._get_request(route=route, params=request_params, **kwargs)

    def get_alerts(self, user_id=None, field=None, request_params=None, **kwargs):
        """
        Returns alerts.
        :param user_id: user ID
        :param field: notification field
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/alerts/{field}"
        return self._get_request(route=route, params=request_params, **kwargs)

    def get_alert_status(self, user_id=None, field=None, request_params=None, **kwargs):
        """
        Returns alert status.
        :param user_id: user ID
        :param field: notification field
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/alerts/{field}"
        return self._get_request(route=route, params=request_params, **kwargs)


class Comment(_Guttr):
    """
    Comment
    """

    def __init__(self):
        _Guttr.__init__(self)

    @paginate
    def get_post_comments(self, comment_id=None, offset=0, maximum=20, direction="rev", request_params=None, follow=False, **kwargs):
        """
        Returns a post comment.
        :param comment_id: comment ID
        :param offset: offset
        :param max: max
        :param direction: direction
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/post/{comment_id}/comments"
        if not request_params:
            request_params = {"offset": offset,
                              "max": maximum,
                              "incl": "commentstats|userinfo|posts|poststats",
                              "dir": direction}
        r = self._get_request(route=route, params=request_params, **kwargs)
        return r.json()

    @paginate
    def get_comment_comments(self, comment_id=None, offset=0, maximum=20, direction="rev", request_params=None, follow=False, **kwargs):
        """
        Returns a post comment.
        :param comment_id: comment ID
        :param offset: offset
        :param max: max
        :param direction: direction
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/comment/{comment_id}/comments"
        if not request_params:
            request_params = {"offset": offset,
                              "max": maximum,
                              "incl": "posts|stats|userinfo|shared|liked|commentstats|userinfo|posts|poststats",
                              "dir": direction}
        r = self._get_request(route=route, params=request_params, **kwargs)
        return r.json()


class Feed(_Guttr):
    """
    Feed
    """

    def __init__(self):
        _Guttr.__init__(self)


class Follow(_Guttr):
    """
    Follow
    """

    def __init__(self):
        _Guttr.__init__(self)

    def get_follow_status(self, user_id=None, follower_id=None, request_params=None, **kwargs):
        """
        Checks if follower_id is following the user_id.
        :param user_id: user ID
        :param follower_id: follower
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{follower_id}/follows/{user_id}"
        r = self._get_request(route=route, params=request_params, **kwargs)
        return r.json()

    @paginate
    def get_follows(self, user_id=None, offset=0, maximum=20, request_params=None, follow=False, **kwargs):
        """
        Returns list of user follows.
        :param user_id: user ID
        :param offset: offset
        :param max: max
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/followings"
        if not request_params:
            request_params = {"offset": offset,
                              "max": maximum,
                              "incl": "userstats|userinfo|followings"}
        r = self._get_request(route=route, params=request_params, **kwargs)
        return r.json()

    @paginate
    def get_followers(self, user_id=None, offset=0, maximum=20, request_params=None, follow=False, **kwargs):
        """
        Returns list of user followers.
        :param user_id: user ID
        :param offset: offset
        :param max: max
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/followers"
        if not request_params:
            request_params = {"offset": offset,
                              "max": maximum,
                              "incl": "userstats|userinfo|followings"}
        r = self._get_request(route=route, params=request_params, **kwargs)
        return r.json()

    def unfollow(self, user_id=None, follower_id=None, request_params=None, **kwargs):
        """
        Unfollow a user.
        ## FIX ME

        :param user_id: user ID
        :param follower_id: follower
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/unfollows/{follower_id}"
        r = self._post_request(route=route, params=request_params, **kwargs)
        return r.json()

    def follow(self, user_id=None, follower_id=None, request_params=None, **kwargs):
        """
        Follow a user.
        ## FIX ME

        :param user_id: user ID
        :param follower_id: follower
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/follows/{follower_id}"
        r = self._post_request(route=route, params=request_params, **kwargs)
        return r.json()


class Like(_Guttr):
    """
    Likes
    """

    def __init__(self):
        _Guttr.__init__(self)

    def like_post(self, user_id=None, post_id=None, request_params=None, **kwargs):
        """
        CLike a post.
        :param user_id: user ID
        :param post_id: post ID
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/likes/post/{post_id}"
        r = self._post_request(route=route, params=request_params, **kwargs)
        return r.json()

    def unlike_post(self, user_id=None, post_id=None, request_params=None, **kwargs):
        """
        Unlike a post.
        :param user_id: user ID
        :param post_id: post ID
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/unlike/post/{post_id}"
        r = self._post_request(route=route, params=request_params, **kwargs)
        return r.json()

    def like_comment(self, user_id=None, comment_id=None, request_params=None, **kwargs):
        """
        Like a comment.
        :param user_id: user ID
        :param comment_id: comment ID
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/likes/post/{comment_id}"
        r = self._post_request(route=route, params=request_params, **kwargs)
        return r.json()

    def unlike_comment(self, user_id=None, comment_id=None, request_params=None, **kwargs):
        """
        Unlike a comment.
        :param user_id: user ID
        :param comment_id: comment ID
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/unlike/post/{comment_id}"
        r = self._post_request(route=route, params=request_params, **kwargs)
        return r.json()

    @paginate
    def get_post_likes_by_user(self, user_id=None, request_params=None, follow=False, **kwargs):
        """
        Get all posts liked by a user.
        :param user_id: user ID
        :param comment_id: comment ID
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/likes/post/"
        if not request_params:
            request_params = {"incl": "posts|poststats"}
        r = self._get_request(route=route, params=request_params, **kwargs)
        return r.json()


class Post(_Guttr):
    """
    Post
    """

    def __init__(self):
        _Guttr.__init__(self)

    def get_post(self, post_id=None, request_params=None, **kwargs):
        """
        Returns a post.
        :param post_id: post ID
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/post/{post_id}"
        r = self._get_request(route=route, params=request_params, **kwargs)
        return r.json()

    @paginate
    def get_user_posts(self, user_id=None, offset=0, maximum=20, direction="rev", request_params=None, follow=False, **kwargs):
        """
        Returns a user's posts.
        :param user_id: user ID
        :param offset: offset
        :param max: max
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/posts"
        if not request_params:
            request_params = {"offset": offset,
                              "max": maximum,
                              "dir": direction,
                              "incl": "posts|stats|userinfo|shared|liked",
                              "fp": "f_uo"}
        r = self._get_request(route=route, params=request_params, **kwargs)
        return r.json()

    @paginate
    def get_post_comments(self, post_id=None, offset=0, maximum=20, direction="rev", request_params=None, follow=False, **kwargs):
        """
        Returns a post's comments.
        :param post_id: post ID
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/post/{post_id}/comments"
        if not request_params:
            request_params = {"offset": offset,
                              "max": maximum,
                              "dir": direction,
                              "incl": "posts|stats|userinfo|shared|liked",
                              "fp": "f_uo"}
        r = self._get_request(route=route, params=request_params, **kwargs)
        return r.json()

    @paginate
    def search_posts(self, query=None, offset=0, maximum=20, request_params=None, **kwargs):
        """
        Searches posts.
        :param post_id: post ID
        :param offset: offset
        :param max: max
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/posts/srch/phrase"
        data = {"content": {"incl": "userinfo|followings|followers", "q": query, "offset": offset, "max": maximum}}
        r = self._post_request(route=route, params=request_params, json=data, **kwargs)
        return r.json()


class Watch(_Guttr):
    """
    Watch
    """

    def __init__(self):
        _Guttr.__init__(self)

    def watch_status(self, post_id=None, user_id=None, request_params=None, **kwargs):
        """
        Returns an object watch stats.
        ## FIX ME

        :param post_id: post ID
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/watch/post/{post_id}"
        r = self._get_request(route=route, params=request_params, **kwargs)
        return r.json()


class User(_Guttr):
    """
    User
    """

    def __init__(self):
        _Guttr.__init__(self)

    @paginate
    def get_mutes(self, user_id=None, offset=0, maximum=20, request_params=None, **kwargs):
        """
        Returns muted users.
        :param user_id: user ID
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/mutes"
        if not request_params:
            request_params = {"offset": offset,
                              "max": maximum,
                              "incl": "userstats|userinfo"}
        r = self._get_request(route=route, params=request_params, **kwargs)
        return r.json()

    @paginate
    def get_blocks(self, user_id=None, offset=0, maximum=20, request_params=None, **kwargs):
        """
        Returns blocked users.
        :param user_id: user ID
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/blockers"
        if not request_params:
            request_params = {"offset": offset,
                              "max": maximum,
                              "incl": "userstats|userinfo"}
        r = self._get_request(route=route, params=request_params, **kwargs)
        return r.json()

    def mute(self, user_id=None, follower_id=None, request_params=None, **kwargs):
        """
        Follow a user.
        :param user_id: user ID
        :param follower_id: follower
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/mutes/{follower_id}"
        r = self._post_request(route=route, params=request_params, **kwargs)
        return r.json()

    def block(self, user_id=None, follower_id=None, request_params=None, **kwargs):
        """
        Follow a user.
        :param user_id: user ID
        :param follower_id: follower
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/blocks/{follower_id}"
        r = self._post_request(route=route, params=request_params, **kwargs)
        return r.json()

    def unmute(self, user_id=None, follower_id=None, request_params=None, **kwargs):
        """
        Follow a user.
        :param user_id: user ID
        :param follower_id: follower
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/mutes/{follower_id}"
        r = self._delete_request(route=route, params=request_params, **kwargs)
        return r.json()

    def unblock(self, user_id=None, follower_id=None, request_params=None, **kwargs):
        """
        Follow a user.
        :param user_id: user ID
        :param follower_id: follower
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/blocks/{follower_id}"
        r = self._delete_request(route=route, params=request_params, **kwargs)
        return r.json()

    @paginate
    def search_users(self, user_id=None, offset=0, maximum=20, request_params=None, **kwargs):
        """
        Searches users.
        :param user_id: user ID
        :param offset: offset
        :param max: max
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/users/srch/phrase"
        data = {"content": {"incl": "userinfo|followings|followers", "q": user_id, "offset": offset, "max": maximum}}
        r = self._post_request(route=route, params=request_params, json=data, **kwargs)
        return r.json()

    def does_user_exist(self, user_id=None, request_params=None, **kwargs):
        """
        Follow a user.
        ## FIX ME

        :param user_id: user ID
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/u/user/{user_id}/exists"
        r = self._get_request(route=route, params=request_params, **kwargs)
        return r.json()

    def does_email_exist(self, email=None, request_params=None, **kwargs):
        """
        Checks if an email is registered.
        :param email: email
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/s/email/exists?email={email}"
        r = self._get_request(route=route, params=request_params, **kwargs)
        return r.json()


class Suggest(_Guttr):
    """
    Suggest
    """

    def __init__(self):
        _Guttr.__init__(self)

    @paginate
    def suggest_user(self, offset=0, maximum=20, request_params=None, **kwargs):
        """
        Returns a list of suggested users.
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/s/usertag/suggest"
        if not request_params:
            request_params = {"offset": offset, "max": maximum, "incl": "userinfo|followings"}
        r = self._get_request(route=route, params=request_params, **kwargs)
        return r.json()

    @paginate
    def suggest_hashtag(self, offset=0, maximum=20, request_params=None, **kwargs):
        """
        Returns a list of suggested hashtags.
        :param request_params: request_params
        :param kwargs:
        :return:
        """
        route = f"/s/hashtag/suggest"
        request_params = {"offset": offset, "max": maximum}
        r = self._get_request(route=route, params=request_params, **kwargs)
        return r.json()
