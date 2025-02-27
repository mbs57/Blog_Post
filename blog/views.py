from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

# View to handle post deletion
def delete_post(request, post_id):
    # Get the post by its ID
    post = get_object_or_404(Post, id=post_id)
    
    # Delete the post
    post.delete()

    # Redirect to the post list page after deletion
    return redirect('post_list')  # Make sure 'post_list' is the correct URL name for your post list view

# View to display the "Add Post" page and save a new post
def add_post(request):
    if request.method == 'POST':
        # Get data from the form
        title = request.POST['title']
        content = request.POST['content']
        
        # Create and save the new post
        new_post = Post(title=title, content=content)
        new_post.save()

        # Redirect to the post list page after saving the post
        return redirect('post_list')  # 'post_list' should match the name of your list view

    # Render the form template for GET requests
    return render(request, 'blog/add_post.html')

