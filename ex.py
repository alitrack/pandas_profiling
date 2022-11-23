from pandas_profiling import ProfileReport
import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])
profile = ProfileReport(df, title="Pandas Profiling Report")
htmlContent = profile.to_html()
from js import document
iframe = document.createElement('iframe')
iframe.width="100%"
iframe.height="600"
document.body.append(iframe)
iframe.contentWindow.document.write(htmlContent)