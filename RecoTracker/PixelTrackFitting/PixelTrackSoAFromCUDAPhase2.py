import FWCore.ParameterSet.Config as cms

def PixelTrackSoAFromCUDAPhase2(**kwargs):
  mod = cms.EDProducer('PixelTrackSoAFromCUDAPhase2',
    src = cms.InputTag('pixelTracksCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
