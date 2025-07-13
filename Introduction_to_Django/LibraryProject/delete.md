```markdown
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
Output:

python
Copy
Edit
#(1, {'bookshelf.Book': 1})

#<QuerySet []>