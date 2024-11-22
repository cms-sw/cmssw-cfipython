import FWCore.ParameterSet.Config as cms

def SiStripTrackingRecHitsValid(*args, **kwargs):
  mod = cms.EDProducer('SiStripTrackingRecHitsValid',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
