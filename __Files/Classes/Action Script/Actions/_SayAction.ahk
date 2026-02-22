
#Include C:\\Users\\felip\\Documents\\GitHub\\oldbot\__Files\Classes\Action Script\Actions\_AbstractActionScript.ahk

class _SayAction extends _AbstractActionScript
{
    static IDENTIFIER := "say"

    __Call(method, args*) {
        methodParams(this[method], method, args)
    }

    /**
    * @return bool
    */
    runAction()
    {
        functionValues := this.values
        this.info(ActionScript.string_log)

        params := {}
            , params.message := functionValues.1
            , params := this.checkParamsVariables(params)


            new _Say(params.message, new _CavebotIniSettings().get("turnChatOffAfterMessages"))

        return true
    }
}