from django.shortcuts import render

# "posts" is a Python "list"
# it is a "list" of "dictionaries"
posts = [
    # dictionary begin ===>>
    {
        # information associated with the "post"
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'Content of the first post',
        'date_posted': 'August 27, 2018',
    },
    # <<=== dictionary end
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Content of the second post',
        'date_posted': 'August 28, 2018',
    },
]


def home(request):
    # let's just pretend for now that we've made a database call and got back this "list" of "posts"
    # and we want to display this post on our blog home page.
    # so, we can pass this "post" into our template just by passing in our argument with that data.
    # and we'll put our data into a dictionary.
    # so, within our home() page view here let's create a dictionary,
    # and we'll call this dictionary a "context".

    context = {
        # and I'll set it equal to a "dictionary"
        # and now within that "context" "dictionary" I'm going to create a "key"
        # and that "key" is going to be called a 'posts':
        'posts': posts,  # and the value I'm going to assign to our "posts" "key"
        # is that list of posts that we've created on the top of the file.

    }

    return render(request, 'blog/home.html', context)  # and now we can pass that "context" in as a
    # third argument to our render function
    # and by doing that it will pass our data into our template and let us access that data within our template


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
