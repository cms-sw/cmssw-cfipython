import FWCore.ParameterSet.Config as cms

def HcalOnlineHarvesting(**kwargs):
  mod = cms.EDProducer('HcalOnlineHarvesting',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
