import StitchSettings from '../components/StitchSettings'
import ThreadColorPicker from '../components/ThreadColorPicker'
import EmbroideryPreview from '../components/EmbroideryPreview'
import ExportSection from '../components/ExportSection'

export default function Editor() {
  return (
    <div className="min-h-screen bg-dark-900 pt-24 pb-16">
      <div className="max-w-7xl mx-auto px-6">
        <h1 className="text-4xl font-bold thread-effect mb-2">Embroidery Editor</h1>
        <div className="grid lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2 space-y-8">
            <EmbroideryPreview />
          </div>
          <div className="space-y-8">
            <StitchSettings />
            <ThreadColorPicker />
            <ExportSection />
          </div>
        </div>
      </div>
    </div>
  )
}
