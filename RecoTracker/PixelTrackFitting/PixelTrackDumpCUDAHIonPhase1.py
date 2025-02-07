import FWCore.ParameterSet.Config as cms

def PixelTrackDumpCUDAHIonPhase1(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelTrackDumpCUDAHIonPhase1',
    onGPU = cms.bool(True),
    pixelTrackSrc = cms.InputTag('pixelTracksCUDA'),
    pixelVertexSrc = cms.InputTag('pixelVerticesCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
