"""Run after `npx cap add android`; adds responsive edge-to-edge UI and app icons."""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1]
android = root / 'android'
main = android / 'app/src/main/java/com/simo/mask/MainActivity.java'
main.parent.mkdir(parents=True, exist_ok=True)
main.write_text('''package com.simo.mask;

import android.os.Bundle;
import android.os.Build;
import androidx.activity.EdgeToEdge;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
  @Override
  public void onCreate(Bundle savedInstanceState) {
    EdgeToEdge.enable(this);
    super.onCreate(savedInstanceState);
    if (Build.VERSION.SDK_INT >= 29) {
      getWindow().setNavigationBarContrastEnforced(false);
    }
  }
}
''', encoding='utf-8')

res = android / 'app/src/main/res'
for density in ('mdpi', 'hdpi', 'xhdpi', 'xxhdpi', 'xxxhdpi'):
    dest = res / f'mipmap-{density}'
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / 'assets' / f'ic_launcher_{density}.png', dest / 'ic_launcher.png')
    shutil.copy2(root / 'assets' / f'ic_launcher_round_{density}.png', dest / 'ic_launcher_round.png')
    shutil.copy2(root / 'assets' / f'ic_launcher_foreground_{density}.png', dest / 'ic_launcher_foreground.png')
print('Configured edge-to-edge and Simo Mask launcher icons')

# Android adaptive icons use the app's purple background and white shield.
colors = res / 'values/ic_launcher_background.xml'
colors.write_text('<?xml version="1.0" encoding="utf-8"?>\n<resources><color name="ic_launcher_background">#5E55E8</color></resources>\n', encoding='utf-8')
