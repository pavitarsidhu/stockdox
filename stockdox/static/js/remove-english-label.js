function filename_without_english (filename) {
	filename = filename.replace("- English", "");

	// This converts stuff like "&amp" to "&" 
	let parser = new DOMParser;
	let dom = parser.parseFromString(
    '<!doctype html><body>' + filename,
    'text/html');
	let decodedString = dom.body.textContent;
	
	return decodedString;
}