#Include C:\\Users\\felip\\Documents\\GitHub\\oldbot\__Files\Classes\Client\Json\_ClientJson.ahk
#Include C:\\Users\\felip\\Documents\\GitHub\\oldbot\__Files\Classes\Config\_Folders.ahk

class _HealingJson extends _ClientJson
{
    static INSTANCE

    __New()
    {
        if (_HealingJson.INSTANCE) {
            return _HealingJson.INSTANCE
        }

        this.file := StrReplace(OldBotSettings.settingsJsonObj.files.healing, ".json", "")

        _HealingJson.INSTANCE := this
    }

    ;#Region Getters
    getFolder()
    {
        return _Folders.JSON_HEALING
    }

    getFile()
    {
        return this.file
    }
    ;#EndRegion
}