function search_company(event) {
	event.preventDefault();
	let companyName = $("#query").val();
	companyName = $.trim(companyName);

	if (companyName) {
		document.getElementById("company-search-button").disabled = true;
		window.location.href="/search/"+companyName;
	}
}

$('#query').keypress(function(e) {
	if (e.which == 13) {
		search_company(e);
	}
});