#Include C:\\Users\\felip\\Documents\\GitHub\\oldbot\__Files\Classes\Config\_AbstractConfigClass.ahk

class _AbstractExecutablesConfig extends _AbstractConfigClass
{
    stopAllExceptOldBot()
    {
        skip := {}
        skip[_OldBotExe.NAME] := true

        this.stopAll(skip)
    }

    stopAll(skip := "")
    {
        for _, exe in this.getList() {
            if (skip[exe.NAME]) {
                continue
            }

            exe.stop()
        }
    }
}
