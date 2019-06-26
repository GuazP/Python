from datetime import datetime as dtfrom math import sqrt as sqimport tkinterimport osclass parameters_cpu:    def __init__(self):        #Create file to hold pc specification        self.time = dt.now()        self.time = self.time.strftime("%H:%M %d.%m.%Y")        self.temp_file = 'temp.txt'        self.main()        os.remove(self.temp_file)        #input("Press enter to continue...")    def main(self):        #CPU model        os.system('sudo dmidecode -t system > ' + self.temp_file)        self.cpu_model()        #Scan disks        #os.system('sudo fdisk -l | grep -i disk > ' + self.temp_file)        os.system('sudo parted -l > ' + self.temp_file) ### < ONLY ONE DISK        self.disc_space_info()        #RAM        os.system('sudo dmidecode -t memory > ' + self.temp_file) ### < ONLY ONE RAM        self.ram_memory_info()        #Processor        os.system('sudo dmidecode -s processor-version > ' + self.temp_file)        os.system('sudo dmidecode -t processor >> ' + self.temp_file)        os.system('lscpu >> ' + self.temp_file)        self.processor_info()        #Graphic card        os.system('sudo lshw -c display > ' + self.temp_file)        self.graphic_card_info()        #Screen resolution        self.screen_resolution_info()        #Wifi        os.system('ifconfig > ' + self.temp_file)        self.check_wifi_access()        #Battery        os.remove(self.temp_file)        for i in os.listdir('/sys/class/power_supply/.'):            if i.startswith('BAT'):                battery_cat = i        get_battery_full_info = ['manufacturer', 'technology', 'model_name', 'energy_full_design', 'energy_full', 'voltage_min_design']        for get in get_battery_full_info:            os.system('sudo cat /sys/class/power_supply/' + battery_cat + '/' + get + ' >> ' + self.temp_file)        self.battery_info()        os.system('sudo dmidecode -t bios > ' + self.temp_file)        self.bios_info()        #BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###        #BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###        #BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###        #BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###        #BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###BIOS###    def cpu_model(self):        try:            #Read /\ for export to precised file            specification = open(self.temp_file, 'r')            grab_value = ('\tManufacturer:', '\tProduct Name:', '\tSerial Number:')            read_model = specification.readlines()            specification.close()            model = open('cpu_model_info.txt', 'w')            #Working loop            for reading in read_model:                for check in grab_value:                    if reading.startswith(check):                        model.write(reading[1:])                        continue                continue            del read_model, grab_value            model.close()        except Exception as model_exception:            self.error_log('cpu_model_info.txt', model_exception)            return 0        print("CPU model has been read")    def disc_space_info(self):        try:            #Read /\ for export to precised file            specification = open(self.temp_file, 'r')            read_disc = specification.readlines()            specification.close()            disc = open('disc_info.txt', 'w')            info = ('Model:', 'Dysk')            #Save contents of command            for line in read_disc:                for check in info:                    if line.startswith(check):                        disc.write(line)            #Working loop            os.system('lsblk -d -o name,model,rota > ' + self.temp_file)            os.system('rm -rf drive_info.txt')            specification = open(self.temp_file, 'r')            read_disc = specification.readlines()            specification.close()            for check in read_disc:                if check.startswith('sd') and "Flash" not in check:                    if check.endswith('1\n'):                        disc.write('Type: HDD\n')                        continue                    elif check.endswith('0\n'):                        disc.write('Type: SSD\n')                        continue                elif check.startswith('sr') or check.startswith('cd') and "DVD" in check or "CD" in check:                    with open('drive_info.txt', 'w') as cd_rom:                        cd_rom.write('Available\n')                        result='available'            del read_disc            try:                cd_rom = open('drive_info.txt', 'r')                cd_rom.close()                result='available'            except FileNotFoundError:                with open('drive_info.txt', 'a+') as cd_rom:                    cd_rom.write('Unvailable\n')                    result='unavailable'            disc.close()        except Exception as disc_exception:            self.error_log('disc_space_info', disc_exception)            return 0        print("Disc has been read")        print("CD_rom has been read and is " + result)    def ram_memory_info(self):        try:            #Read /\ for export to precised file            specification = open(self.temp_file, 'r')            #Temp            ram = open('ram_info.txt', 'w')            temp = ''            temp2 = ''            read_file = specification.readlines()            specification.close()            #Working loop            for check in read_file:                check = check.partition(': ')                #print(check)                if check[0].endswith('Size'):                    check = check[2][0:-3]                    if check[0].isdigit():                        #print(check)                        temp += 'Memory size: ' + str(round(int(check)/1024,1))+'GB'                elif check[0].endswith('Type'):                    if check[2].startswith('DD'):                        temp += '\nMemory type: '+check[2]            ram.write(temp)            del (temp, read_file)            ram.close()        except Exception as ram_exception:            self.error_log('ram_memory_info', ram_exception)            return 0        print("RAM memory has been read")    def processor_info(self):        try:            #Read /\ for export to precised file            specification = open(self.temp_file, 'r')            grab_value = ('Model name:', 'Model:', 'Architecture:', '\tCore Enabled:', '\tCore Count:', '\tThread Count:', '\tMax Speed:')            #Temp            proc = open('proc_info.txt', 'w')            read_file = specification.readlines()            specification.close()            #Working loop            for reading in read_file:                for check in grab_value:                    if reading.startswith(check):                        while '\t' in reading:                            reading = reading.replace('\t', '')                        while '  ' in reading:                            reading = reading.replace('  ', ' ')                        proc.write(reading)                        continue                continue            del read_file, grab_value            proc.close()        except Exception as proc_exception:            self.error_log('processor_info', proc_exception)            return 0        print("Processor has been read")    def graphic_card_info(self):        try:            #Read /\ for export to precised file            specification = open(self.temp_file, 'r')            read_file = specification.readlines()            specification.close()            #Temp            graph = open('graphic_info.txt', 'w')            temp = ''            temp2 = ''            #Working loop            for check in read_file:                check = check.partition(': ')                if check[0].endswith('product'):                    temp += check[2]                if check[0].endswith('vendor'):                    check = check[2].partition('\n')                    temp2 += check[0]+" "+temp                    break            graph.write(temp2)            del (temp, temp2, read_file)            graph.close()        except Exception as graphic_exception:            self.error_log('graphic_card_info', graphic_exception)            return 0        print("Graphic card has been read")    def screen_resolution_info(self):        mm_to_inch = 0.039        try:            import subprocess            screens = [i.split()[-3::2] for i in subprocess.check_output(["xrandr"]).decode("utf-8").splitlines() if " connected" in i]            max_resolution = [i.split()[0] for i in subprocess.check_output(["xrandr"]).decode('utf-8').splitlines() if 'x' in i][2]            #print(max_resolution)            screen = open('screen_info.txt', 'w')            for num, s in enumerate(screens,1):                s[0] = float(s[0].replace("mm", ""))                s[1] = float(s[1].replace("mm", ""))                scr_size = (((s[0]**2)+(s[1]**2))**(0.5))*mm_to_inch                screen.write('Rozmiar monitora ' + str(num) + ': ~' + str(round(scr_size,1)) + '\n')                screen.write('Maksymalna rozdzielczość: ' + max_resolution)            screen.close()        except Exception as screen_exception:            self.error_log('screen_resolution_info', screen_exception)            return 0        print("Screen resolution has been read")    def check_wifi_access(self):        try:            specification = open(self.temp_file, 'r')            check = specification.readlines()            specification.close()            check_var = 0            wifi = open('wifi_check.txt', 'w')            for temp in check:                if temp.startswith('w'):                    wifi.write('Available\n')                    check_var += 1                    result = 'available'                    break            if check_var == 0:                wifi.write('unavailable\n')                result = 'unavailable'            del (check, check_var)            wifi.close()        except Exception as wifi_exception:            self.error_log('wifi_access', wifi_exception)            return 0        print("Wifi access has been read and is " + result)        del result    def battery_info(self):            #get_battery_full_info = ['producent', 'technologia', 'model_name', 'energy_full_design', 'enegy_full', 'voltage_min_design']        try:            organize_data = ('Producent: ', 'Model i typ: ', 'Maxymalna pojemność zaprojektowana/obecna: ', 'Napięcie do ładowania: ')            specification = open(self.temp_file, 'r')            battery = open('battery_info.txt', 'w')            check = specification.readline()            #Working loop            for i in organize_data:                battery.write(i+check[:-1])                if i.startswith("Model"):                    check = specification.readline()[:-1]                    battery.write(' ' + check)                elif i.startswith("Max"):                    temp_max = int(check)                    check = specification.readline()                    temp_now = int(check)                    temp = 'Wydajność baterii: '+str(int(round(temp_now/temp_max,2)*100))+'%'                    battery.write(' / ' + check + temp)                    del(temp_max, temp_now, temp)                battery.write('\n')                check = specification.readline()        except Exception as battery_exception:            self.error_log('battery_info', battery_exception)            return 0        print("Battery has been read")    def bios_info(self):        try:            specification = open(self.temp_file, "r")            bios = open('bios_info.txt', "w")            check = specification.readlines()            specification.close()            for i in check[5:12]:                if i.startswith('\t'):                    bios.write(i[1:])                else:                    bios.write(i)            bios.close()            del check        except Exception as bios_exception:            self.error_log('bios_info', bios_exception)            return 0        print("Bios has been read")    def error_log(self, function, error):        print(str(error) + '\nCheck error log!')        log = open('Error_log.txt', 'a')        log.write('{}# in function {}\n{}\nFile named: {}\n'.format(self.time, function, str(error), str(__file__)))        return 0    def return_tag(self):        with open('cpu_model_info.txt', 'r') as serw:            lines = serw.readlines()            for line in lines:                if 'Serial' in line:                    serwis_tag = line[15:]                    print(serwis_tag)        return str(serwis_tag)if __name__ == "__main__":    parameters_cpu()            #One disc, other with path os.listdir and many loops...            #os.system('cat /sys/block/sda/queue/rotational > ' + self.temp_file)            #temp=open(self.temp_file, 'r')            #if temp.read(1)=='1':                #disc.write('Typ: HDD')            #else:                #disc.write('Typ: SSD')