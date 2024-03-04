import FWCore.ParameterSet.Config as cms

def PixelTrackSoAFromCUDAPhase1(**kwargs):
  mod = cms.EDProducer('PixelTrackSoAFromCUDAPhase1',
    src = cms.InputTag('pixelTracksCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
