import FWCore.ParameterSet.Config as cms

def PixelTrackDumpCUDAPhase2(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelTrackDumpCUDAPhase2',
    onGPU = cms.bool(True),
    pixelTrackSrc = cms.InputTag('pixelTracksCUDA'),
    pixelVertexSrc = cms.InputTag('pixelVerticesCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
