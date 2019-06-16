import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;

import java.net.MalformedURLException;
import java.net.URL;


public class SimpleTest {

    @Test
    public void pageShouldContainExpectedMessage() throws InterruptedException {
        String actualMessage = driver.findElement(By.cssSelector("*")).getText();

        String expectedMessage = "check for this message"; //TODO: put the correct message here

        assert (actualMessage.contains(expectedMessage)) : String.format("Message '%s' was not found on the page, but was instead '%s'", expectedMessage, actualMessage);
        Thread.sleep(5000); //Added for demo purposes
    }

    @Before
    public void setUp() throws MalformedURLException {
        driver = new RemoteWebDriver(new URL("http://selenium:4444/wd/hub"), capability);
        driver.get("http://webserver:5000");
    }

    @After
    public void tearDown() {
        driver.quit();
    }

    RemoteWebDriver driver;
    DesiredCapabilities capability = DesiredCapabilities.firefox();

}