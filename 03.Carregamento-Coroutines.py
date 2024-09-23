import kotlinx.coroutines.*
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import android.widget.TextView

class AsyncActivity : AppCompatActivity() {

    private lateinit var resultTextView: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_async)

        resultTextView = findViewById(R.id.resultTextView)

        // Iniciar carregamento assíncrono
        CoroutineScope(Dispatchers.IO).launch {
            val data = fetchData()
            withContext(Dispatchers.Main) {
                resultTextView.text = data
            }
        }
    }

    private suspend fun fetchData(): String {
        delay(2000) // Simular tempo de carregamento
        return "Dados carregados"
    }
}


