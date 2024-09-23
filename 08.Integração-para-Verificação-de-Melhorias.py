import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import android.widget.TextView

class SummaryActivity : AppCompatActivity() {

    private lateinit var summaryTextView: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_summary)

        summaryTextView = findViewById(R.id.summaryTextView)

        // Exibe as melhorias implementadas e seus resultados
        val summary = """
            1. Tempo de carregamento reduzido em 30%.
            2. Vazamentos de memória corrigidos.
            3. Interface mais fluida e responsiva.
            4. Notificações push otimizadas para melhor performance.
        """.trimIndent()

        summaryTextView.text = summary
    }
}
