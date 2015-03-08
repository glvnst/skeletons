TARGETS=js/main.js css/main.css
.PHONY: all clean loop

all: $(TARGETS)

clean:
	rm -f $(TARGETS)

loop:
# fixme: choose a real watcher program and use that
# facebook watchman is overkill
	while true; do make -s; sleep 3; done

js/%.js: %.coffee
	@echo "$$(date) - Rebuilding $@"
	coffee -b -c -o js -m $<

css/%.css: %.sass
	@echo "$$(date) - Rebuilding $@"
	sass $< $@
