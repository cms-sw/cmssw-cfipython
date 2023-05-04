import FWCore.ParameterSet.Config as cms

pixelTrackDumpCUDAPhase2 = cms.EDAnalyzer('PixelTrackDumpCUDAPhase2',
  onGPU = cms.bool(True),
  pixelTrackSrc = cms.InputTag('pixelTracksCUDA'),
  pixelVertexSrc = cms.InputTag('pixelVerticesCUDA'),
  mightGet = cms.optional.untracked.vstring
)
