#Include C:\\Users\\felip\\Documents\\GitHub\\oldbot\__Files\Components\_AbstractControl.ahk

class _NumberEdit extends _Edit
{
    ; __Call(method, args*) {
    ;     methodParams(this[method], method, args)
    ; }

    __New()
    {
        base.__New()

        this.numeric()
    }
}
