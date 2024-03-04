import FWCore.ParameterSet.Config as cms

def PixelTrackDumpCUDAHIonPhase1(**kwargs):
  mod = cms.EDAnalyzer('PixelTrackDumpCUDAHIonPhase1',
    onGPU = cms.bool(True),
    pixelTrackSrc = cms.InputTag('pixelTracksCUDA'),
    pixelVertexSrc = cms.InputTag('pixelVerticesCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
