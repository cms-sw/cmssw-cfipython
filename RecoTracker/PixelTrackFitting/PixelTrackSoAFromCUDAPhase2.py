import FWCore.ParameterSet.Config as cms

def PixelTrackSoAFromCUDAPhase2(*args, **kwargs):
  mod = cms.EDProducer('PixelTrackSoAFromCUDAPhase2',
    src = cms.InputTag('pixelTracksCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
