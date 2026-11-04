![KukySolutions, com o avatar original em amarelo e roxo e a Drippy, assistente do OneDrip](assets/banner.png)

# KukySolutions

**Software útil. Projetos com personalidade.**

Desenvolvo o **OneDrip**, a assistente **Drippy** e projetos que tornam o computador um lugar mais interessante, como a **Bolha**.

[OneDrip](https://onedrip.com.br) · [Conheça a Drippy](https://onedrip.com.br/drippy) · [Código da Bolha](https://github.com/kuky13/bolha)

## OneDrip: da entrada do aparelho à entrega

Uma plataforma para assistências técnicas de celulares e eletrônicos: orçamentos, ordens de serviço, clientes, peças e atendimento organizados em um só lugar.

[![Demonstração pública do OneDrip: orçamentos e ordens de serviço, com dados fictícios identificados como simulação](assets/onedrip-demo.jpg)](https://onedrip.com.br)

*Captura da apresentação pública do OneDrip. Simulação com dados fictícios.*

O produto é desenvolvido em repositórios privados.

[Conhecer o OneDrip](https://onedrip.com.br) · [Explorar o OneDrip Parts](https://onedrip.com.br/parts)

## Drippy: uma conversa, uma colmeia de especialistas

![A Drippy do OneDrip, gatinha de óculos e moletom verde água, acompanhada das abelhas de orçamentos, atendimento, peças e ajuda](assets/drippy-colmeia.png)

A Drippy é a assistente de IA do OneDrip. A colmeia organiza módulos especializados para ajudar com **orçamentos, mensagens, peças, imagens, pesquisa, ajuda e diagnóstico Android**.

No código, um núcleo encaminha os pedidos aos especialistas, com mensagens correlacionadas e ferramentas do produto. Algumas tarefas usam regras e buscas locais; outras consultam serviços de IA. Cada pedido usa a ajuda de que precisa.

Você confere os resultados e decide o que fazer. Na pesquisa de peças, fontes e evidências ajudam a avaliar a compatibilidade, que precisa ser verificada.

[Conhecer a Drippy e a colmeia](https://onedrip.com.br/drippy)

## Bolha: companhia para o seu desktop

Um pet experimental para Windows que passeia pela tela, reage ao carinho, brinca e aprende com suas interações.

![Prévia da Bolha sem boca, com olhos e orelhas em três estados: tranquila, feliz e dormindo](assets/bolha-qt-preview.png)

*Prévia visual da versão 0.3.0 em desenvolvimento, desenhada em Qt. A migração nativa ainda está em andamento; o download aponta para a versão publicada.*

A versão publicada **0.2.1 usa Electron e React**. A versão **0.3.0, em desenvolvimento**, prepara a migração para **Python + Qt/PySide6**, com emoções, objetivos e memória locais.

[Código da versão publicada](https://github.com/kuky13/bolha) · [Ver versões e download](https://github.com/kuky13/bolha/releases/latest)

## Uma base que merece crédito

A Bolha utiliza uma adaptação do motor do Pestinha, criado pelo [autor original](https://github.com/mille-okws) e seus contribuidores. A origem e as licenças estão documentadas no projeto.

[Conhecer o Pestinha](https://github.com/mille-okws/pestinha) · [Consultar os créditos da Bolha](https://github.com/kuky13/bolha/blob/main/NOTICE.md)

## Tecnologias dos projetos

| Onde | Tecnologias e uso |
|---|---|
| Interface do OneDrip | TypeScript, React, Vite, Tailwind CSS e Radix UI |
| Dados e backend | Supabase, PostgreSQL e funções em Deno/TypeScript |
| Estado e consultas | TanStack Query e Zustand |
| Integrações | IA, WhatsApp e diagnóstico Android com ADB/WebUSB |
| Qualidade | Vitest, Playwright e ESLint |
| Bolha nativa, em desenvolvimento | Python, Qt/PySide6 e PyInstaller |

<sub>[Origem e atribuição das imagens](assets/README.md)</sub>
