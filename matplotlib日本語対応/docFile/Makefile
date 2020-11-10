doc.pdf: doc.dvi
	dvipdfmx doc.dvi
	rm doc.dvi

doc.dvi: doc.tex
	platex -interaction=batchmode doc.tex
	platex -interaction=batchmode doc.tex
