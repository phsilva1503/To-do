# To-do


Virtual enviroment

python -m ven ven

.venv\Scripts\activate

CASO ERRO: 

 .venv\Scripts\activate : O arquivo C:\Users\Pedro\git\to-do-list\.venv\Scripts\Activate.ps1 não pode ser carregado porque a execução de scripts foi desabilitada     
neste sistema. Para obter mais informações, consulte about_Execution_Policies em https://go.microsoft.com/fwlink/?LinkID=135170.
No linha:1 caractere:1
+ .venv\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ErrodeSegurança: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess

    ENTÃO --> NO POWER SHELL  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

    