
#Include, C:\\Users\\felip\\Documents\\GitHub\\oldbot\__Files\Classes\Cavebot\Walkable Conditions\_AbstractWalkableCondition.ahk

class _CavebotWalkerCondition extends _AbstractWalkableCondition
{
    __Call(method, args*) {
        methodParams(this[method], method, args)
    }

    handle()
    {
        if (!CavebotWalker.isCoordWalkable(this.x, this.y, this.z)) {
            return false
        }

        return true
    }
}