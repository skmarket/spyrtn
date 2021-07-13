.PHONY: chapter4 lint preinstall

chapter4: preinstall
ifeq ($(OS),Windows_NT)
	@python -m pytest && echo ready to submit! || echo answer may wrong ...
else
	@python3 -m pytest && echo "提出の準備完了です！" || echo "\n--- 期待した答えになっていないようです。コードを確認してください --\n\n\n"
endif

lint:
ifeq ($(OS),Windows_NT)
	@python -m flake8 || (echo "-- make sure your code format --"; exit 1)
else
	@python3 -m flake8 || (echo "\n-- 上のメッセージを参考に、コード規約を確認してください --\n\n\n"; exit 1)
endif

preinstall:
	@pip3 install -q -r requirements.txt