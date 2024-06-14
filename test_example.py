import re
from playwright.sync_api import Page, expect
from playwright.sync_api import  expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    
# def test_search_and_play_rickroll():
#     with sync_playwright() as p:
#         # Launch browser
#         browser = p.chromium.launch(headless=False)  # Set headless=True if you don't want to see the browser window
#         context = browser.new_context()
#         page = context.new_page()

#         # Go to YouTube
#         page.goto("https://www.youtube.com/")

#         # Search for "Rick Astley - Never Gonna Give You Up"
#         search_box = page.locator('input#search')
#         search_box.fill('Rick Astley - Never Gonna Give You Up')
#         search_button = page.locator('button#search-icon-legacy')
#         search_button.click()

#         # Wait for the results to load and click on the first video
#         page.wait_for_selector('ytd-video-renderer')
#         first_video = page.locator('ytd-video-renderer').first
#         first_video.click()

#         # Wait for the video to start playing
#         page.wait_for_selector('video')

#         # Assert that the video is playing
#         video_element = page.locator('video')
#         expect(video_element).to_be_visible()

#         # Optionally, you can wait for a few seconds to see the video play
#         page.wait_for_timeout(5000)  # Wait for 5 seconds

#         # Close the browser
#         browser.close()

# if __name__ == "__main__":
#     import pytest
#     pytest.main()   

