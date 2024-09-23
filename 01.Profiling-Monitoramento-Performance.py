import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import android.os.Debug
import android.util.Log

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Iniciar Profiling
        Debug.startMethodTracing("app_trace")

        // Simulação de carga de trabalho
        for (i in 0..1000) {
            Log.d("MainActivity", "Processing item: $i")
        }

        // Parar Profiling
        Debug.stopMethodTracing()
    }
}