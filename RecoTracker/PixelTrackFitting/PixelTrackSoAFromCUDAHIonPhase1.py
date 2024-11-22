import FWCore.ParameterSet.Config as cms

def PixelTrackSoAFromCUDAHIonPhase1(*args, **kwargs):
  mod = cms.EDProducer('PixelTrackSoAFromCUDAHIonPhase1',
    src = cms.InputTag('pixelTracksCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
