
<h1>Proje Adı</h1>

<h2>Açıklama</h2>
<p>Varsayılan olarak Gaussian bulanıklık seviyesi "yüksek" olarak ayarlanmıştır ve bu seviyeye göre bulanıklık uygulanır. Kod, OpenCV kütüphanesini kullanarak bulanıklaştırma işlemini gerçekleştirir.</p>

<h2>Nasıl Kullanılır</h2>
<ol>
<li><strong>Gereksinimler</strong>
    <ul>
        <li>Python 3.x</li>
        <li>OpenCV</li>
        <li>NumPy</li>
    </ul>
</li>

<li><strong>Kurulum</strong>
    <pre><code>pip install opencv-python numpy</code></pre>
</li>

<li><strong>Kod Açıklaması</strong>
    <ul>
        <li><code>apply_gaussian_blur(image, level='high')</code>: Görüntüyü belirtilen Gaussian bulanıklık seviyesine göre bulanıklaştırır.</li>
        <li><code>copy_txt_file(src_path, dest_path)</code>: Metin dosyasını belirtilen hedefe kopyalar.</li>
        <li><code>startProcess(inn, out)</code>: Belirtilen klasördeki JPG dosyalarını bulanıklaştırır ve aynı klasördeki metin dosyalarını başka bir klasöre kopyalar.</li>
    </ul>
</li>

<li><strong>Kullanım</strong>
    <ol>
        <li><code>ornek_resimler</code> klasörüne işlem yapılacak JPG ve TXT dosyalarını yerleştirin.</li>
        <li>Betiği çalıştırarak <code>output</code> klasöründe işlenmiş dosyaları gözlemleyin.</li>
    </ol>
</li>

<li><strong>Örnek Kullanım</strong>
    <pre><code>python script.py</code></pre>
</li>
</ol>

<h2>Lisans</h2>
<p>Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için <a href="./LICENSE">LICENSE</a> dosyasına göz atabilirsiniz.</p>
