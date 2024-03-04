import FWCore.ParameterSet.Config as cms

def SiStripRecHitsValid(**kwargs):
  mod = cms.EDProducer('SiStripRecHitsValid',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
