import FWCore.ParameterSet.Config as cms

def SiPixelTrackingRecHitsValid(**kwargs):
  mod = cms.EDProducer('SiPixelTrackingRecHitsValid',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
