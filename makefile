name=
url=
all:
	 you-gt $(url) && mencoder -forceidx -of lavf -oac mp3lame -lameopts abr:br=24 -ovc copy -o $(name).flv `ls *.flv` && rm -rf *_* && mv *.flv ../

blank:	
	for f in *; do mv "$$f" `echo $$f | tr ' ' '_'`; done
