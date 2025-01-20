const urlParams = new URLSearchParams(window.location.search)
console.log(urlParams)
const pmc = urlParams.get('pmc')
document.getElementById('pmc').innerText = pmc
graph(document.getElementById('main'), pmc + '.json')

async function show_missing() {
  const missing = await GET(pmc + "-missing.json", '')
  console.log(missing)
  var html = "<ul>"
  for (key in missing) {
    html += "<li>" + key + " (found in " + missing[key] + ")</li>"
  }
  html += "</ul>"
	console.log(html)

  document.getElementById('missing').innerHTML = html
}
show_missing()
