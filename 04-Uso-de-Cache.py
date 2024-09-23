import android.graphics.Bitmap
import android.util.LruCache

class ImageCache {

    private val cache: LruCache<String, Bitmap>

    init {
        // Calcular o tamanho máximo do cache
        val maxMemory = (Runtime.getRuntime().maxMemory() / 1024).toInt()
        val cacheSize = maxMemory / 8

        cache = object : LruCache<String, Bitmap>(cacheSize) {
            override fun sizeOf(key: String, bitmap: Bitmap): Int {
                return bitmap.byteCount / 1024
            }
        }
    }

    fun getBitmap(key: String): Bitmap? {
        return cache.get(key)
    }

    fun putBitmap(key: String, bitmap: Bitmap) {
        cache.put(key, bitmap)
    }
}
