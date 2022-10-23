dia_i = int(input().split(" ")[1])
hi, mi, si = map(int, input().split(":"))
dia_f = int(input().split(" ")[1])
hf, mf, sf = map(int, input().split(":"))

si = si + (mi*60) + (hi*60*60) + (dia_i*24*60*60)
sf = sf + (mf*60) + (hf*60*60) + (dia_f*24*60*60)

dif_s = sf - si

dia_t = dif_s // (24*60*60)
dif_s = dif_s % (24*60*60)

hora_t = dif_s // (60*60)
dif_s = dif_s % (60*60)

min_t = dif_s // 60
dif_s = dif_s % 60

seg_f = dif_s

print(f'{dia_t} dia(s)')
print(f'{hora_t} hora(s)')
print(f'{min_t} minuto(s)')
print(f'{seg_f} segundo(s)')