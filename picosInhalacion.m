%fn='primera medicion awm2100/cerca exhalacion positiva.abf';
%fn='primera medicion awm2100/lejos exhalacion positiva.abf';
cut=strfind(fn,'.');
fnOut=[fn(1:cut-1) '.txt'];
[d,si,h]=abfload(fn);

t = (0:si/1000:(length(d)-1)*si/1000)/1000;

%% CARGO DATOS

clear all
data = load('AWM3100/trazoN33.txt', '-ascii');

t = data(:,1)/1000;
d = data(:,2);

clear data 

plot(t,d)

%%

sampleRate=30000;
y=sgolayfilt(d,2,0.1*sampleRate+1);
y=y';
yDetrend=locdetrend(y,sampleRate,[1.5 .5]);

figure;
hold on
subplot(2,1,1)
plot(t,yDetrend)
subplot(2,1,2)
plot(t,d)
hold off

%%
minSeparation=1/12;
[inhalVal inhalInd] = findpeaks(yDetrend','MinPeakDistance',round(minSeparation*sampleRate),'MinPeakProminence',0.75*std(yDetrend),'MinPeakHeight',0);

zci = @(v) find(v(:).*circshift(v(:), [-1 0]) <= 0);                    % Returns Zero-Crossing Indices Of Argument Vector
zeroCrossInd = zci(yDetrend);    

startInhalInd=nan(length(inhalInd),1);
startExhalInd=nan(length(inhalInd),1);
for i=1:length(inhalInd)
    startInhalInd(i)=zeroCrossInd(find(inhalInd(i)>=zeroCrossInd,1,'last'));
    startExhalInd(i)=zeroCrossInd(find(inhalInd(i)<=zeroCrossInd,1,'first'));
end

figure(10); plot(t,-yDetrend)
hold on
plot(t(inhalInd),-yDetrend(inhalInd),'xk')
plot(t(startInhalInd),-yDetrend(startInhalInd),'og')
plot(t(startExhalInd),-yDetrend(startExhalInd),'or')
xlabel('Tiempo (s)')

%%

minSeparation=1/12;
[inhalVal inhalInd] = findpeaks(-d,'MinPeakDistance',round(minSeparation*sampleRate),'MinPeakProminence',0.75*std(yDetrend),'MinPeakHeight',0);

zci = @(v) find(v(:).*circshift(v(:), [-1 0]) <= 0);                    % Returns Zero-Crossing Indices Of Argument Vector
zeroCrossInd = zci(d);    

startInhalInd=nan(length(inhalInd),1);
startExhalInd=nan(length(inhalInd),1);
for i=1:length(inhalInd)
    startInhalInd(i)=zeroCrossInd(find(inhalInd(i)>=zeroCrossInd,1,'last'));
    startExhalInd(i)=zeroCrossInd(find(inhalInd(i)<=zeroCrossInd,1,'first'));
end

figure(10); plot(t,d)
hold on
plot(t(inhalInd),d(inhalInd),'xk')
plot(t(startInhalInd),d(startInhalInd),'og')
plot(t(startExhalInd),d(startExhalInd),'or')
xlabel('Tiempo (s)')



%% EXPORTAR A TXT

fnOut = 'procesado.txt';
data = [t;yDetrend];
fileID = fopen(fnOut,'w');
fprintf(fileID,'%12s %12s \n', 't(ms)','filtrado(mV)');
fprintf(fileID,'%12.6f %12.6f \n', data);
fclose(fileID);
fnOut = 'procesado.mat';
save(fnOut,'data');

fnOut = 'inhalaciones.txt';
puntos = [ix;iy;fx;fy;px;py];
fileID = fopen(fnOut,'w');
fprintf(fileID,'%12s %12s %12s %12s %12s %12s\n', 'ix','iy','fx','fy','px','py');
fprintf(fileID,'%12.6f %12.6f %12.6f %12.6f %12.6f %12.6f\n', puntos);
fclose(fileID);
fnOut = 'inhalaciones.mat';
save(fnOut,'puntos');


