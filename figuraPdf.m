function figuraPdf(figureName)
set(gcf,'PaperOrientation','landscape');
%print(gcf, '-dpdf', '-r300','-bestfit',figureName);
print(gcf, '-dpdf', '-r300','-fillpage',figureName);
