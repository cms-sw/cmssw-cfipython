import FWCore.ParameterSet.Config as cms

def HcalRecHitsClient(**kwargs):
  mod = cms.EDProducer('HcalRecHitsClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
