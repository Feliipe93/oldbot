#include C:\Users\felip\Documents\GitHub\oldbot\__Files\Shared\OldBot\Settings\Objects\_DefaultValue.ahk

class _DefaultBoolean extends _DefaultValue
{
    ; __Call(method, args*) {
    ;     methodParams(this[method], method, args)
    ; }

    /**
    * @param mixed default
    * @param ?string identifier
    */
    __New(default, identifier := "")
    {
        base.__New(default, 0, 1, identifier)
    }
}