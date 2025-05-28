// Injetor de html
function injetorHTML(url, id) {
  fetch(url)
    .then((response) => response.text())

    .then((html) => {
      document.getElementById(id).innerHTML = html;
    })
    .catch((error) => {
      console.log("Erro ao carregar conteudo", error);
    });
}
