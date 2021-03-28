#run:
#	@python3 predict.py
bin/run: src/run.cpp
	@mkdir -p bin
	@g++ $^ -o bin/run

run: bin/run
	@bin/run
