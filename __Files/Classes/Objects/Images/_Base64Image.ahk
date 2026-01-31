
#Include C:\Users\Alfredo\Documents\GitHub\oldbot\__Files\Shared\OldBot\ImageSearch\_AbstractBase64Image.ahk

class _Base64Image extends _AbstractBase64Image
{
	__New(name := "", base64 := "") {
		base.__New(name, base64, this)
	}

	/**
	* @abstract
	* @return void
	*/
	disposeImageFromCache() {
	}
}