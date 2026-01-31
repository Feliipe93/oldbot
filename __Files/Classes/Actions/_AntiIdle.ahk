

#Include C:\Users\Alfredo\Documents\GitHub\oldbot\__Files\Classes\Actions\_AbstractAction.ahk

class _AntiIdle extends _AbstractAction
{
    __Call(method, args*) {
        methodParams(this[method], method, args)
    }

    run()
    {
        try {
            r := random(0, 1)
            SendModifier("Ctrl", r ? "Up" : "Left")
            sleep(50, 100)
            SendModifier("Ctrl", r ? "Down" : "Right")
        } catch e {
            this.handleException(e, this)
            throw e
        }
    }
}