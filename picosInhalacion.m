fn='primera medicion awm2100/cerca exhalacion positiva.abf';
%fn='primera medicion awm2100/lejos exhalacion positiva.abf';
cut=strfind(fn,'.');
fnOut=[fn(1:cut-1) '.txt'];
[d,si,h]=abfload(fn);

t = (0:si/1000:(length(d)-1)*si/1000)/1000;

sampleRate=30000;
y=sgolayfilt(d,2,0.1*sampleRate+1);
y=y';
yDetrend=locdetrend(y,sampleRate,[1.5 .5]);

minSeparation=1/12;
[inhalVal inhalInd]=findpeaks(-yDetrend,'MinPeakDistance',round(minSeparation*sampleRate),'MinPeakProminence',.75*std(yDetrend),'MinPeakHeight',0);

zci = @(v) find(v(:).*circshift(v(:), [-1 0]) <= 0);                    % Returns Zero-Crossing Indices Of Argument Vector
zeroCrossInd = zci(yDetrend);    

startInhalInd=nan(length(inhalInd),1);
startExhalInd=nan(length(inhalInd),1);
for i=1:length(inhalInd)
    startInhalInd(i)=zeroCrossInd(find(inhalInd(i)>=zeroCrossInd,1,'last'));
    startExhalInd(i)=zeroCrossInd(find(inhalInd(i)<=zeroCrossInd,1,'first'));
end

figure; plot(t,yDetrend)
hold on
plot(t(inhalInd),yDetrend(inhalInd),'xk')
plot(t(startInhalInd),yDetrend(startInhalInd),'og')
plot(t(startExhalInd),yDetrend(startExhalInd),'or')
xlabel('Tiempo (s)')