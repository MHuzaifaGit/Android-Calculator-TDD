package com.example.calculatorapp

import androidx.test.espresso.Espresso.onView
import androidx.test.espresso.action.ViewActions.click
import androidx.test.espresso.assertion.ViewAssertions.matches
import androidx.test.espresso.matcher.ViewMatchers.withId
import androidx.test.espresso.matcher.ViewMatchers.withText
import androidx.test.ext.junit.rules.ActivityScenarioRule
import androidx.test.ext.junit.runners.AndroidJUnit4
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
class MainActivityTest {

    @get:Rule
    val activityRule = ActivityScenarioRule(MainActivity::class.java)

    @Test
    fun testAddition() {
        // Click number buttons
        onView(withId(R.id.button5)).perform(click())
        onView(withId(R.id.buttonAdd)).perform(click())
        onView(withId(R.id.button3)).perform(click())
        onView(withId(R.id.buttonEquals)).perform(click())

        // Check result
        onView(withId(R.id.resultTextView)).check(matches(withText("8.0")))
    }

    @Test
    fun testClearButton() {
        // Enter some numbers
        onView(withId(R.id.button7)).perform(click())
        onView(withId(R.id.button2)).perform(click())

        // Clear
        onView(withId(R.id.buttonClear)).perform(click())

        // Check result is reset
        onView(withId(R.id.resultTextView)).check(matches(withText("0")))
    }
}
