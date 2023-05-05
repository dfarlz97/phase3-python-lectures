'''
{
author: {
    name: 
}
post: {
    author: 1 
}
tags: 

}
'''

authors = [
    {'id': 1, 'userName': 'author 1', 'repYear': 2014},
    {'id': 2, 'userName': 'author 2', 'repYear': 2007},
    {'id': 3, 'userName': 'author 3', 'repYear': 2019}
]

posts = [
    {'id': 1, 'content': 'post by author 1', 'postYear': 2014, 'authorId': 1},
    {'id': 2, 'content': 'post by author 1', 'postYear': 2015, 'authorId': 1},
    {'id': 3, 'content': 'post by author 2', 'postYear': 2000, 'authorId': 2}
]
'''
postToTag table

postID | tagId
1          1
1          2
3          1

tag 
id tagText
'''

tags = [
    {'id': 1, 'tagText': 'tag1', 'postId': 1},
    {'id': 2, 'tagText': 'tag2', 'postId': 1},
    {'id': 3, 'tagText': 'tag1', 'postId': 3},
]
def select(FROM, COLUMNS): 
    for item in FROM: 
        for col in COLUMNS: 
            print(item[col])
select(FROM-authors, COLUMNS=["userName", "id"])

for author in authors: 
    if author["repYear"] < 2010:
        print(author)
print(type(authors))
print(authors[0]['repYear'])

for author in authors: 
    for post in posts: 
        for tag in tags:
            if author['id'] == post['authorID'] or post['id'] or tag['postID']:
                print("{} {} {}".format(author, post, tag))
        
    

