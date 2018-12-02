%% Fitteo de los datos de escala

data = csvread('escala-0024/escala.csv');

v_in = data(:,1);
v_out = data(:,2);

c = polyfit(v_out,v_in,1);

disp(['Ec. del fit es y = ' num2str(c(1)) '*x + ' num2str(c(2))])

x_fit = min(v_out):0.1:max(v_out);
y_fit = polyval(c,x_fit);

hold on
plot(v_out,v_in,'ro')
plot(x_fit,y_fit,'r-','LineWidth',1)
xlabel('Vout')
ylabel('Vin')
grid()
hold off

%% Re-escaleo los datos

fn = 'AWM2100/datos-sin-escala/lejos_exh_pos.abf';
[d,si,h] = abfload(fn);
t = [0:si/1000000:(length(d)-1)*si/1000000]';

%d2 = polyval(c,d(:,2));
d2 = polyval(c,d);

figure;
hold on
%plot(t,d(:,2),'k-');
plot(t,d,'k-');
plot(t,d2,'r-')
xlabel('Tiempo (s)')
ylabel('Voltaje (mV)')
hold off

%% Filtro y guardo los datos

fil = designfilt('bandstopiir','FilterOrder',10,'HalfPowerFrequency1',50-2,'HalfPowerFrequency2',50+2, 'DesignMethod','butter','SampleRate',20000);
temp_filt = filtfilt(fil,d2);
temp_filt=d2;
fLowPass=2000;
[b1, a1] = butter(3, fLowPass/(20000*2), 'low');
temp_filt = filter(b1, a1,single(temp_filt));
temp_filt = flipud(temp_filt);
temp_filt = filter(b1, a1, temp_filt);
temp_filt = flipud(temp_filt);

figure; 
h1=subplot(2,1,1);
plot(t,d2);
xlabel('Tiempo (s)')
ylabel('Voltaje (mV)')
h2=subplot(2,1,2);
plot(t,temp_filt)
linkaxes([h1 h2],'xy')
xlabel('Tiempo (s)')
ylabel('Voltaje (mV)')

%% EXPORTAR A TXT
cut=strfind(fn,'.');
fnOut=[fn(1:cut-1) '.txt'];
data=[t*1000;d(:,2)';temp_filt'];
fileID = fopen(fnOut,'w');
fprintf(fileID,'%12s %12s %12s\n','t(ms)','PreFiltro(mV)','PostFiltro(mV)');
fprintf(fileID,'%12.2f %12.6f %12.6f\n',data);
fclose(fileID);
fnOut=[fn(1:cut-1) '.mat'];
save(fnOut,'data');














