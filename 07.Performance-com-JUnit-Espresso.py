import androidx.test.espresso.Espresso.onView
import androidx.test.espresso.action.ViewActions.click
import androidx.test.espresso.matcher.ViewMatchers.withId
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.rule.ActivityTestRule
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
class PerformanceTest {

    @Rule
    @JvmField
    var activityRule: ActivityTestRule<MainActivity> = ActivityTestRule(MainActivity::class.java)

    @Test
    fun testButtonPerformance() {
        val startTime = System.currentTimeMillis()
        onView(withId(R.id.myButton)).perform(click())
        val endTime = System.currentTimeMillis()
        val duration = endTime - startTime
        assert(duration < 500) // Verifica se a ação foi realizada em menos de 500ms
    }
}


