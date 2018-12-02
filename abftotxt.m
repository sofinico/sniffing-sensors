%% Cargo los datos

clear all
fn='AWM2100/datos-sin-escala/lejos_exh_pos.abf';
[d,si,h]=abfload(fn);
t = [0:si/1000000:(length(d)-1)*si/1000000]';

%%

figure;
plot(t,d);
xlabel('Tiempo (s)')
ylabel('Voltaje (mV)')

%% EXPORTAR A TXT

cut=strfind(fn,'.');
fnOut=[fn(1:cut-1) '.txt'];
data=[t*1000,d]';    
fileID = fopen(fnOut,'w');
fprintf(fileID,'%12s %12s\n','t(ms)','IN 5 (mV)');
fprintf(fileID,'%12.2f %12.6f\n',data);
fclose(fileID);
fnOut=[fn(1:cut-1) '.mat'];
save(fnOut,'data');
