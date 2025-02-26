import JSZip from "jszip";

export type SkinPath = {
    download_url: string;
    filename: string;
}

export function downloaSkins(skins: SkinPath[]){
    skins.forEach( skin =>
        downloaSkin(skin)
    )
}

async function downloaSkin(skin: SkinPath):Promise<boolean>{
    const {download_url, filename} = skin;
    const response = await fetch(download_url);
    const skinZipBlob = await response.blob();
    const zip = await JSZip.loadAsync(skinZipBlob);

    const pattern = /\.[mM]$/; // Ganti dengan pattern yang Anda cari

    // Cek apakah file dengan pattern tertentu ada
    const files = zip.file(pattern);

    if (files && files.length > 0) {
        console.log(filename, 'File ditemukan:', files.length, files);
        fetch("/res/add", {
            method: "POST",
            body: JSON.stringify({
                download_url, 
                filename,
                userId: 1,
                title: "Fix my bugs",
                completed: false
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
          });
    } else {
        // console.log('File tidak ditemukan');
    }
    return files && files.length > 0
}