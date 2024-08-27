import FWCore.ParameterSet.Config as cms

def PixelTrackDumpCUDAPhase2(**kwargs):
  mod = cms.EDAnalyzer('PixelTrackDumpCUDAPhase2',
    onGPU = cms.bool(True),
    pixelTrackSrc = cms.InputTag('pixelTracksCUDA'),
    pixelVertexSrc = cms.InputTag('pixelVerticesCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
