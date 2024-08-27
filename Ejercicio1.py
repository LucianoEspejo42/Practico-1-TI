import wave
import struct

def validar_archivo_wav(filename):
    try:
        with open(filename, 'rb') as file:
            # Leer los primeros 12 bytes
            header = file.read(12)
            
            # Verificar que los primeros 4 bytes son "RIFF"
            if header[:4].decode('ascii') != 'RIFF':
                return False

            # Verificar que los bytes 8 a 12 son "WAVE"
            if header[8:12].decode('ascii') != 'WAVE':
                return False
            
            return True
    
    except Exception as e:
        print(f"Error al verificar el archivo: {e}")
        return False

def mostrar_cabecera_wav(filename,name):
    try:
        with open(filename, 'rb') as wav_file:
            cabecera = []
            # RIFF Header
            cabecera.append(f"Nombre del archivo: {name}")
            cabecera.append("|--------------RIFF Header--------------|")
            riff = wav_file.read(44)
            cabecera.append(f"Chunk ID (RIFF): {riff[:4].decode('ascii')}")
            #print(f"Chunk ID (RIFF): {riff[:4].decode('ascii')}")
            chunk_size = struct.unpack('<I', riff[4:8])[0]
            cabecera.append(f"Chunk Size: {chunk_size}")
            format = riff[8:12].decode('ascii')
            cabecera.append(f"Format: {format} (.wav)")

            cabecera.append("|--------------fmt subchunk--------------|")
            # fmt Subchunk
            fmt_subchunk = riff
            cabecera.append(f"Subchunk1 ID (fmt): {fmt_subchunk[12:16].decode('ascii')}")
            subchunk1_size = struct.unpack('<I', fmt_subchunk[16:20])[0]
            cabecera.append(f"Subchunk1 Size: {subchunk1_size}")
            audio_format = struct.unpack('<H', fmt_subchunk[20:22])[0]
            cabecera.append(f"Audio Format: {audio_format}")
            num_channels = struct.unpack('<H', fmt_subchunk[22:24])[0]
            cabecera.append(f"Num Channels (1: Mono, 2: Stereo): {num_channels}")
            sample_rate = struct.unpack('<I', fmt_subchunk[24:28])[0]
            cabecera.append(f"Sample Rate: {sample_rate} Hz")
            byte_rate = struct.unpack('<I', fmt_subchunk[28:32])[0]
            cabecera.append(f"Byte Rate: {byte_rate} bytes/second")
            block_align = struct.unpack('<H', fmt_subchunk[32:34])[0]
            cabecera.append(f"Block Align: {block_align} bytes")
            bits_per_sample = struct.unpack('<H', fmt_subchunk[34:36])[0]
            cabecera.append(f"Bits per Sample: {bits_per_sample} bits")

            cabecera.append("|--------------data--------------|")
            # data Subchunk
            data_subchunk = riff
            cabecera.append(f"Subchunk2 ID (data): {data_subchunk[36:40].decode('ascii')}")
            subchunk2_size = struct.unpack('<I', data_subchunk[40:44])[0]
            cabecera.append(f"Subchunk2 Size: {subchunk2_size} bytes")
            #print(f"Data (first 10 bytes): {data_subchunk[8:18]}")

            return "\n".join(cabecera)
            
            
    except wave.Error as e:
        print(f"Error al procesar el archivo .wav: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")



