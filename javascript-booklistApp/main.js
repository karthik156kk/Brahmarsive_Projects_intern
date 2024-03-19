function Book(title, author, publications){
    this.title = title;
    this.author = author;
    this.publications = publications;
}

class UI{
    static displayBooks(){
        const StoredBooks = [
            {
                title: "Book 1",
                author: "karthik",
                publications: "1324"
            },
            {
                title: "Book 2",
                author: "kausik",
                publications: "2143"
            }
            ]
        const books = StoredBooks;
        books.forEach((book) => UI.addBookToList(book));
    }
    static addBookToList(book){
        const list = document.querySelector('#book-list');
        const row = document.createElement('tr');
        row.innerHTML = `
        <td>${book.title}</td>
        <td>${book.author}</td>
        <td>${book.publications}</td>
        <td><a href="#" class="btn btn-danger delete">Delete</a></td>
        `
        list.appendChild(row);
    }
    static deleteBook(el){
        if(el.classList.contains('delete')){
            el.parentElement.parentElement.remove();
        }
    }
    static clearFields(){
        document.querySelector('#title').value = '';
        document.querySelector('#author').value = '';
        document.querySelector('#publ').value = '';
    }
    static alertMsg(message, className){
        const div = document.createElement('div');
        div.className = `alert ${className}`;
        div.appendChild(document.createTextNode(`${message}`));
        const container = document.querySelector('#container');
        const table = document.querySelector('.table');
        container.insertBefore(div,table);

        setTimeout(()=>document.querySelector('.alert').remove(), 3000);
    }
}

document.addEventListener('DOMContentLoaded', UI.displayBooks);
document.querySelector('#book-form').addEventListener('submit', (e)=>{
    e.preventDefault();
    const title = document.querySelector('#title').value;
    const author = document.querySelector('#author').value;
    const publications = document.querySelector('#publ').value;

    if(title==='' || author==='' || publications===''){
        UI.alertMsg('Please add the fields', 'alert-danger');
    }
    else{
        const book = new Book(title, author, publications);
        UI.addBookToList(book);
        UI.alertMsg('Succesfully added the books', 'alert-success');
        UI.clearFields();
    }
});
document.querySelector('#book-list').addEventListener('click', (e)=>
{
    UI.deleteBook(e.target);
});
