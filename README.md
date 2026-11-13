![KukySolutions, com o avatar original em amarelo e roxo e a Drippy do OneDrip](assets/banner.png)

# KukySolutions

**Software útil. Projetos com personalidade.**

Desenvolvo o **OneDrip**, a assistente **Drippy** e a **Bolha**, uma mascote de código aberto para Windows e Android.

[OneDrip](#onedrip) · [Drippy e a colmeia](#drippy-e-a-colmeia) · [Bolha](#bolha) · [Tecnologias](#tecnologias)

## OneDrip

Gestão para assistências técnicas de celulares e eletrônicos: orçamentos, ordens de serviço, clientes, peças e atendimento em um só lugar.

[Conhecer o OneDrip](https://onedrip.com.br) · [Conhecer o OneDrip Parts](https://onedrip.com.br/parts)

[![Demonstração do OneDrip com orçamentos e ordens de serviço. Simulação com dados fictícios.](assets/onedrip-demo.jpg)](https://onedrip.com.br)

*Demonstração pública com dados fictícios.*

## Drippy e a colmeia

A **Drippy é a assistente de IA do OneDrip**. Sua colmeia reúne especialistas para apoiar orçamentos, atendimento, pesquisa de peças e o uso do sistema.

![Drippy, gatinha de óculos e moletom verde água, com as abelhas de orçamentos, mensagens, peças e ajuda](assets/drippy-colmeia.png)

Você confere os resultados e decide o que fazer. Na pesquisa de peças, consulte as fontes e verifique a compatibilidade.

[Conhecer a Drippy e a colmeia](https://onedrip.com.br/drippy)

## Bolha

Uma mascote que passeia pela tela, brinca com um amendoim e aprende com carinho e outras interações. O cérebro de 470 neurônios roda no próprio aparelho.

**Versão publicada: 0.4.10**, com instalador Windows e APK Android.

![Oito expressões da Bolha: repouso, piscadela, carinho, susto, bocejo, soluço, sono e mastigação](assets/bolha-050-expressoes.png)

*Prévia da 0.5.0 em preparação. A boca fica fechada em repouso e abre por instantes em reações como susto e bocejo. A próxima versão também traz uma Central e um painel neural no Android.*

[Baixar a versão estável](https://github.com/kuky13/bolha/releases/latest) · [Explorar o código](https://github.com/kuky13/bolha) · [Acompanhar a 0.5.0](https://github.com/kuky13/bolha/pull/4)

### Créditos da Bolha

A Bolha é um fork comunitário baseado no sistema do [Pestinha](https://github.com/mille-okws/pestinha), criado por [mille-okws](https://github.com/mille-okws) com a colaboração da comunidade. O cérebro, a física e partes da aplicação do Pestinha foram a base para desenvolver a Bolha.

O código, as artes e as animações próprias da Bolha são abertas sob GPL versão 3 ou posterior, a mesma licença do Pestinha. Contribuições da comunidade são bem vindas. Os guias privados de referência da Drippy não são publicados. Veja os [créditos e licenças](https://github.com/kuky13/bolha/blob/main/NOTICE.md).

## Tecnologias

| Área | Tecnologias e uso |
|---|---|
| Interface do OneDrip | TypeScript, React, Vite, Tailwind CSS e Radix UI |
| Dados e backend | Supabase, PostgreSQL e funções em Deno/TypeScript |
| Estado e consultas | TanStack Query e Zustand |
| Integrações | IA, WhatsApp e diagnóstico Android com ADB/WebUSB |
| Qualidade | Vitest, Playwright e ESLint |
| Bolha | Python, NumPy e Qt/PySide6 no Windows; Java, Canvas e Chaquopy no Android |

[Origem e atribuição das imagens](assets/README.md)

*Versão estável conferida em 13 de novembro de 2026.*
