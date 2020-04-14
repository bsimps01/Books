# Books

## How would we filter for all books with titles containing the word ‘Django’?

    We would filter for all the books with titles containing the word Django such as calling it like this:

    Django = Book.objects.filter(title__contains="Django")

## How would we filter for all books with tag ‘Fiction’?

    Fiction = Book.objects.filter(tags__contains="Fiction")

## How would we filter for all authors who have written books containing the word ‘Django’? HINT: We can use the book field to refer to an author’s books, even though the Author model doesn’t explicitly contain it!

    Authors = Authors.objects.filter(title__contains = "Django")