import FWCore.ParameterSet.Config as cms

def PixelTrackSoAFromCUDAHIonPhase1(**kwargs):
  mod = cms.EDProducer('PixelTrackSoAFromCUDAHIonPhase1',
    src = cms.InputTag('pixelTracksCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
