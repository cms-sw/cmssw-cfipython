import FWCore.ParameterSet.Config as cms

pixelTrackDumpCUDAHIonPhase1 = cms.EDAnalyzer('PixelTrackDumpCUDAHIonPhase1',
  onGPU = cms.bool(True),
  pixelTrackSrc = cms.InputTag('pixelTracksCUDA'),
  pixelVertexSrc = cms.InputTag('pixelVerticesCUDA'),
  mightGet = cms.optional.untracked.vstring
)
