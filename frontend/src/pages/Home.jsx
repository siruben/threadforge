export default function Home() {
  return (
    <div className="min-h-screen bg-dark-900">
      <nav className="fixed top-0 w-full z-50 bg-dark-900/80 backdrop-blur-md border-b border-dark-700">
        <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-gradient-to-br from-thread-600 to-thread-700 rounded-lg flex items-center justify-center">
              <span className="text-white font-bold">TF</span>
            </div>
            <h1 className="text-2xl font-bold thread-effect">ThreadForge</h1>
          </div>
        </div>
      </nav>

      <section className="min-h-screen pt-32 pb-20 px-6">
        <div className="max-w-6xl mx-auto text-center">
          <h2 className="text-5xl md:text-7xl font-bold mb-6 thread-effect">Convert SVG to Embroidery</h2>
          <p className="text-xl text-gray-400 max-w-2xl mx-auto">Upload SVG logos and generate machine-ready embroidery files.</p>

          <div className="mt-12">
            <div className="border-2 border-dashed rounded-2xl p-12">
              <p className="text-gray-400">Drop your logo here</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}
