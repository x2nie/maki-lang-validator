import struct

class MakiFile:
    def __init__(self, file_path):
        self.file = open(file_path, 'rb')  # Buka file dalam mode baca biner

    def close(self):
        self.file.close()  # Tutup file

    def getPosition(self):
        # Kembalikan posisi saat ini dalam file
        return self.file.tell()

    def skip(self, bytes):
        # Lompati sejumlah byte tertentu (relatif terhadap posisi saat ini)
        self.file.seek(bytes, 1)  # `1` berarti relatif terhadap posisi saat ini

    def jump(self, position):
        # Lompat ke posisi tertentu dalam file (absolut)
        self.file.seek(position, 0)  # `0` berarti absolut dari awal file

    def readInt32LE(self):
        # Baca 32-bit signed integer (little endian)
        data = self.file.read(4)
        return struct.unpack('<i', data)[0]

    def readUint32LE(self):
        # Baca 32-bit unsigned integer (little endian)
        data = self.file.read(4)
        return struct.unpack('<I', data)[0]

    def readInt16LE(self):
        # Baca 16-bit signed integer (little endian)
        data = self.file.read(2)
        return struct.unpack('<h', data)[0]

    def readUint16LE(self):
        # Baca 16-bit unsigned integer (little endian)
        data = self.file.read(2)
        return struct.unpack('<H', data)[0]

    def readInt8(self):
        # Baca 8-bit signed integer
        data = self.file.read(1)
        return struct.unpack('<b', data)[0]

    def readUint8(self):
        # Baca 8-bit unsigned integer
        data = self.file.read(1)
        return struct.unpack('<B', data)[0]

    def readString(self):
        # Baca Pascal string (byte pertama adalah panjang string)
        length = self.readUint16LE()  # Panjang string (1 byte)
        string_data = self.file.read(length)  # Baca string sesuai panjang
        return string_data.decode('utf-8')  # Decode ke string UTF-8
    
    def isEof(self):
        # Simpan posisi saat ini
        current_position = self.file.tell()
        
        # Coba baca 1 byte untuk mengecek EOF
        data = self.file.read(1)
        
        if not data:
            # Jika tidak ada data yang dibaca, artinya sudah EOF
            return True
        else:
            # Kembalikan posisi ke sebelumnya
            self.file.seek(current_position, 0)
            return False

if __name__ == '__main__':
    # Contoh penggunaan
    file_path = 'example.bin'  # Ganti dengan path file biner Anda
    reader = MakiFile(file_path)

    # Contoh membaca data
    print("Posisi awal:", reader.getPosition())
    print("Int32 (LE):", reader.readInt32LE())
    print("Posisi setelah baca Int32:", reader.getPosition())

    reader.jump(8)  # Lompat ke posisi 8 (absolut dari awal file)
    print("Posisi setelah jump ke 8:", reader.getPosition())

    print("Uint16 (LE):", reader.readUint16LE())
    print("Pascal String:", reader.readPascalString())

    # Jangan lupa tutup file setelah selesai
    reader.close()