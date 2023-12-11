// script.js 파일 내용
let btnradio1 = document.getElementById('btnradio1');
let btnradio2 = document.getElementById('btnradio2');
let btnradio3 = document.getElementById('btnradio3');
let searchContainer = document.getElementById('searchContainer');
let btnGroup1 = document.getElementById('btnGroup1');
let btnGroup2 = document.getElementById('btnGroup2');
let dataTable = document.getElementById('dataTable');

btnradio1.addEventListener('click', function() {
    searchContainer.style.display = 'block';
    btnGroup1.style.display = 'none';
    btnGroup2.style.display = 'none';
    dataTable.style.display = 'none';
});

btnradio2.addEventListener('click', function() {
    searchContainer.style.display = 'none';
    btnGroup1.style.display = 'block';
    btnGroup2.style.display = 'block';
    dataTable.style.display = 'none';
});

btnradio3.addEventListener('click', function() {
    searchContainer.style.display = 'none';
    btnGroup1.style.display = 'none';
    btnGroup2.style.display = 'none';
    dataTable.style.display = 'table';
});
