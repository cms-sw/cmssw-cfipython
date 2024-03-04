import FWCore.ParameterSet.Config as cms

def HcalOfflineHarvesting(**kwargs):
  mod = cms.EDProducer('HcalOfflineHarvesting',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
