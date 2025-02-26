import { downloaSkins, SkinPath } from "./skins"

export function setupCounter(element: HTMLButtonElement) {
    let amount = 0
    const setCounter = (count: number) => {
        amount = count
        element.innerHTML = `loading ${amount} skins`
    }
    // element.addEventListener('click', () => setCounter(amount))
    element.addEventListener('click', async () => {
        const skins = await loadSkins(amount);
        downloaSkins(skins)
    })
    setCounter(100)
}

function gql(strings: TemplateStringsArray): string {
    return strings[0];
}

async function loadSkins(amount: number):Promise<SkinPath[]> {
    const query = `
      query {
        modern_skins(first: ${amount}) {
          nodes {
            filename
            download_url
          }
        }
      }
    `;

    console.log(query)
  
    let bankskin1 = [];
    try {
      const response = await fetch("https://api.webampskins.org/graphql", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        mode: "cors",
        credentials: "include",
        body: JSON.stringify({ query, variables: {} }),
      });
      const data = await response.json();
      bankskin1 = data.data.modern_skins.nodes;
    } catch (e) {
      console.warn('faile to load skins from api.webampskins.org')
    }

    console.log(bankskin1)
    return bankskin1 as SkinPath[]
}