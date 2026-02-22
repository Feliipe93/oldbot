#Include C:\\Users\\felip\\Documents\\GitHub\\oldbot\__Files\Classes\_Market\Objects\Item Offer\_ItemOffer.ahk

class _BuyItemOffer extends _ItemOffer
{
    __Call(method, args*) {
        methodParams(this[method], method, args)
    }

    __New(item)
    {
        base.__New(item, "buy", "sell")
    }

    rejectOffer(price)
    {
        if (price > this.getPrice()) {
            throw Exception(txt("preço da oferta é maior do que o preço desejado", "offer price is higher than the desired price")	" (" price " > " this.getPrice() ").")
        }
    }

    offerFulfilledEvent(amount)
    {
        this.incrementFulfilledAmount(amount)
    }

    resetProgress()
    {
        this.settings("boughtAmount", 0)
    }

    ;#region Getters
    getFulfilledAmountKey()
    {
        return "boughtAmount"
    }

    getDisplayAction()
    {
        return txt("comprar", "buy")
    }

    getActionIdentifier()
    {
        return "buy"
    }
    ;#endregion
}