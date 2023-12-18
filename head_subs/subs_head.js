const fs = require('fs');
const path = require('path');
const { Input } = require('enquirer');

const novoHead = `
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Pedagogia em espaços não escolares</title>
	<!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css"> -->
	<link rel="stylesheet" href="./assets/css/bulma.min.css">
	<link rel="stylesheet" href="./assets/css/header-intro.css">
	<link rel="stylesheet" href="./assets/css/custom.css">
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Ubuntu" >
	<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Karla" >
	<link href="https://fonts.googleapis.com/css2?family=Secular+One&display=swap" rel="stylesheet">
	<link rel="stylesheet" href="photoswipe/dist/photoswipe.css">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="https://unpkg.com/photoswipe@5.2.2/dist/photoswipe.css">
</head>
`;

async function substituirHeadArquivos() {
    const diretorioAtual = process.cwd();  // Pega o diretório atual onde o script está sendo executado
    const arquivos = fs.readdirSync(diretorioAtual);

    for (const arquivo of arquivos) {
        if (arquivo.endsWith(".html")) {
            const caminhoArquivo = path.join(diretorioAtual, arquivo);
            let conteudo = fs.readFileSync(caminhoArquivo, 'utf-8');

            // Substitua o bloco <head> no modelo
            const novoConteudo = conteudo.replace(/<head>[\s\S]*?<\/head>/i, novoHead);
            fs.writeFileSync(caminhoArquivo, novoConteudo, 'utf-8');
        }
    }

    const input = new Input({
        message: 'Digite o título do livro:',
        name: 'tituloLivro'
    });

    const resposta = await input.run();

    for (const arquivo of arquivos) {
        if (arquivo.endsWith(".html")) {
            const caminhoArquivo = path.join(diretorioAtual, arquivo);
            let conteudo = fs.readFileSync(caminhoArquivo, 'utf-8');

            // Substitua o bloco <title> pelo título fornecido pelo usuário
            const novoConteudo = conteudo.replace(/<title>[\s\S]*?<\/title>/i, `<title>${resposta}</title>`);
            fs.writeFileSync(caminhoArquivo, novoConteudo, 'utf-8');
        }
    }
}

substituirHeadArquivos();

