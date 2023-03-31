import FWCore.ParameterSet.Config as cms

pixelTrackDumpCUDAPhase1 = cms.EDAnalyzer('PixelTrackDumpCUDAPhase1',
  onGPU = cms.bool(True),
  pixelTrackSrc = cms.InputTag('pixelTracksCUDA'),
  pixelVertexSrc = cms.InputTag('pixelVerticesCUDA'),
  mightGet = cms.optional.untracked.vstring
)
