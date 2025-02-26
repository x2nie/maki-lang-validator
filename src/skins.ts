import JSZip from "jszip";

export type SkinPath = {
    download_url: string;
    filename: string;
}

export function downloaSkins(skins: SkinPath[]){
    skins.forEach( skin =>
        downloaSkin(skin.download_url)
    )
}

async function downloaSkin(skinPath: string){
    const response = await fetch(skinPath);
    const skinZipBlob = await response.blob();
    const zip = await JSZip.loadAsync(skinZipBlob);

    const pattern = /\.m/; // Ganti dengan pattern yang Anda cari

    // Cek apakah file dengan pattern tertentu ada
    const files = zip.file(pattern);

    if (files) {
        console.log(skinPath, 'File ditemukan:', files.length);
    } else {
        // console.log('File tidak ditemukan');
    }
}