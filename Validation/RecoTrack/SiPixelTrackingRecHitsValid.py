import FWCore.ParameterSet.Config as cms

def SiPixelTrackingRecHitsValid(*args, **kwargs):
  mod = cms.EDProducer('SiPixelTrackingRecHitsValid',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
