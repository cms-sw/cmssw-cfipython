import FWCore.ParameterSet.Config as cms

def HcalRealisticZS(**kwargs):
  mod = cms.EDProducer('HcalRealisticZS',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
