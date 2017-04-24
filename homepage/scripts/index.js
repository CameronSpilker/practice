$(function(){
console.log('in console');
	$('#search-button').click(function(){
		console.log('hi');
		var search = $('#search-input').val();
		console.log('this is the search input', search);
		var url = '/homepage/index.search/' + search
		window.location.replace(url);
 	
});//click



});//ready function