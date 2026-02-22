#Include, C:\\Users\\felip\\Documents\\GitHub\\oldbot\__Files\Classes\Cavebot\Walkable Conditions\_AbstractWalkableCondition.ahk

class _SpecialAreaCondition extends _AbstractWalkableCondition
{
    __Call(method, args*) {
        methodParams(this[method], method, args)
    }

    handle()
    {

    }
}