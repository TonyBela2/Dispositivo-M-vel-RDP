import org.apache.jmeter.config.Arguments
import org.apache.jmeter.control.LoopController
import org.apache.jmeter.protocol.http.control.HeaderManager
import org.apache.jmeter.protocol.http.sampler.HTTPSamplerProxy
import org.apache.jmeter.samplers.SampleResult
import org.apache.jmeter.threads.ThreadGroup

class LoadTestConfig {

    fun createTestPlan(): TestPlan {
        // Configurações de amostrador HTTP
        val httpSampler = HTTPSamplerProxy()
        httpSampler.domain = "www.reidopitaco.com"
        httpSampler.path = "/api/load"
        httpSampler.method = "GET"

        // Configurações de controlador de loop
        val loopController = LoopController()
        loopController.loops = 100

        // Configurações de grupo de threads
        val threadGroup = ThreadGroup()
        threadGroup.numThreads = 10
        threadGroup.rampUp = 5
        threadGroup.sampleErrorThreshold = 0.05

        // Configurações de plano de teste
        val testPlan = TestPlan("Teste de Carga")
        testPlan.addTestElement(httpSampler)
        testPlan.addTestElement(loopController)
        testPlan.addTestElement(threadGroup)

        return testPlan
    }
}
