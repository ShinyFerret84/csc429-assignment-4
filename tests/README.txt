--------------------------------------------------------------------------------
TEST CASE 1: Linux Student Developer
--------------------------------------------------------------------------------
Input Profile:
  - Budget Level: Low ("budget_low")
  - Portability Important: Yes ("portable")
  - Primary Usage: Basic Office / Study Only ("office_only")
  - OS Preference: Linux ("pref_os_linux")

Initial Facts Array:
  ['budget_low', 'portable', 'office_only', 'pref_os_linux']

Execution Trace:
  Step 1: Fired 'Student Light Office' (Priority 5)
          IF ['budget_low', 'office_only', 'portable'] THEN recommend:budget_ultrabook
  Step 2: Fired 'Linux Suitability' (Priority 2)
          IF ['pref_os_linux', 'office_only'] THEN spec:linux_friendly_hw

Expected Conclusions:
  - Recommendation : Budget Ultrabook
  - Specification  : Linux Friendly HW


--------------------------------------------------------------------------------
TEST CASE 2: High-End Creative Workstation (No Gaming)
--------------------------------------------------------------------------------
Input Profile:
  - Budget Level: High ("budget_high")
  - Portability Important: Yes ("portable")
  - Primary Usage: Creative Work / Video Editing ("creative_work")
  - Large Screen (15"+): Yes ("large_screen")
  - Hardware Requirement: AI Acceleration ("needs_ai_accel")

Initial Facts Array:
  ['budget_high', 'portable', 'creative_work', 'large_screen', 'needs_ai_accel']

Execution Trace:
  Step 1: Fired 'Creative Work (RAM)' (Priority 3)
          IF ['creative_work', 'portable'] THEN spec:ram_16_plus
  Step 2: Fired 'Creative Work (Display)' (Priority 3)
          IF ['creative_work', 'large_screen'] THEN spec:display_15_plus_color_accurate
  Step 3: Fired 'AI Acceleration' (Priority 3)
          IF ['needs_ai_accel'] THEN spec:gpu_with_tensor_cores

Expected Conclusions:
  - Recommendation : None derived from given criteria
  - Specifications : 16GB+ RAM, 15"+ Color Accurate Display, GPU with Tensor Cores


--------------------------------------------------------------------------------
TEST CASE 3: Road Warrior Mac User
--------------------------------------------------------------------------------
Input Profile:
  - Budget Level: High ("budget_high")
  - Portability Important: Yes ("portable")
  - Battery Need: Long Battery Life ("long_battery")
  - Travel Frequency: Travel Often ("travel_often")
  - OS Preference: macOS ("pref_os_macos")

Initial Facts Array:
  ['budget_high', 'portable', 'long_battery', 'travel_often', 'pref_os_macos']

Execution Trace:
  Step 1: Fired 'Budget Ultra-portable' (Priority 5)
          IF ['budget_high', 'portable', 'long_battery'] THEN recommend:premium_ultrabook
  Step 2: Fired 'Travel + Battery' (Priority 3)
          IF ['travel_often', 'long_battery'] THEN spec:battery_60wh_plus
  Step 3: Fired 'OS Preference macOS' (Priority 2)
          IF ['pref_os_macos'] THEN spec:macos_required

Expected Conclusions:
  - Recommendation : Premium Ultrabook
  - Specifications : 60Wh+ Battery, macOS Required


--------------------------------------------------------------------------------
TEST CASE 4: Midrange Casual Gamer & Traveler
--------------------------------------------------------------------------------
Input Profile:
  - Budget Level: Medium ("budget_medium")
  - Primary Usage: Gaming ("gaming")
  - Travel Frequency: Travel Often ("travel_often")
  - Battery Need: Long Battery Life ("long_battery")

Initial Facts Array:
  ['budget_medium', 'gaming', 'travel_often', 'long_battery']

Execution Trace:
  Step 1: Fired 'Midrange Gaming' (Priority 4)
          IF ['gaming', 'budget_medium'] THEN recommend:midrange_gaming_laptop
  Step 2: Fired 'Travel + Battery' (Priority 3)
          IF ['travel_often', 'long_battery'] THEN spec:battery_60wh_plus

Expected Conclusions:
  - Recommendation : Midrange Gaming Laptop
  - Specification  : 60Wh+ Battery


--------------------------------------------------------------------------------
TEST CASE 5: Non-Portable Linux Office Desktop
--------------------------------------------------------------------------------
Input Profile:
  - Portability Important: No ("portable" absent)
  - Primary Usage: Basic Office / Study Only ("office_only")
  - OS Preference: Linux ("pref_os_linux")

Initial Facts Array:
  ['office_only', 'pref_os_linux']

Execution Trace:
  Step 1: Fired 'Linux Suitability' (Priority 2)
          IF ['pref_os_linux', 'office_only'] THEN spec:linux_friendly_hw

Expected Conclusions:
  - Recommendation : None derived from given criteria
  - Specification  : Linux Friendly HW


--------------------------------------------------------------------------------
TEST CASE 6: All-Round Power User (Pro Gaming + Creative + AI)
--------------------------------------------------------------------------------
Input Profile:
  - Budget Level: High ("budget_high")
  - Primary Usage: Gaming ("gaming")
  - Primary Usage: Creative Work / Video Editing ("creative_work")
  - Portability Important: Yes ("portable")
  - Large Screen (15"+): Yes ("large_screen")
  - Hardware Requirement: AI Acceleration ("needs_ai_accel")

Initial Facts Array:
  ['budget_high', 'gaming', 'creative_work', 'portable', 'large_screen', 'needs_ai_accel']

Execution Trace:
  Step 1: Fired 'Pro Gaming' (Priority 5)
          IF ['gaming', 'budget_high'] THEN recommend:high_end_gaming_laptop
  Step 2: Fired 'Creative Work (RAM)' (Priority 3)
          IF ['creative_work', 'portable'] THEN spec:ram_16_plus
  Step 3: Fired 'Creative Work (Display)' (Priority 3)
          IF ['creative_work', 'large_screen'] THEN spec:display_15_plus_color_accurate
  Step 4: Fired 'AI Acceleration' (Priority 3)
          IF ['needs_ai_accel'] THEN spec:gpu_with_tensor_cores

Expected Conclusions:
  - Recommendation : High End Gaming Laptop
  - Specifications : 16GB+ RAM, 15"+ Color Accurate Display, GPU with Tensor Cores