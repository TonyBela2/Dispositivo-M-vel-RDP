import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class DetailsActivity : AppCompatActivity() {

    private var dataLoader: DataLoader? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_details)

        dataLoader = DataLoader()
        dataLoader?.loadData()
    }

    override fun onDestroy() {
        super.onDestroy()
        // Liberar recursos para evitar vazamento de memória
        dataLoader?.cancel()
        dataLoader = null
    }
}

class DataLoader {
    fun loadData() {
        // Simular carregamento de dados
    }

    fun cancel() {
        // Cancelar carregamento de dados
    }
}



