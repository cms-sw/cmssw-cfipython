import FWCore.ParameterSet.Config as cms

def SiStripRecHitsValid(*args, **kwargs):
  mod = cms.EDProducer('SiStripRecHitsValid',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
