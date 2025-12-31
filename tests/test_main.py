from hello_antigravity.main import main

def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello world at GitHub!"
