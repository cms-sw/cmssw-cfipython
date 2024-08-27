import FWCore.ParameterSet.Config as cms

def SiStripTrackingRecHitsValid(**kwargs):
  mod = cms.EDProducer('SiStripTrackingRecHitsValid',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
