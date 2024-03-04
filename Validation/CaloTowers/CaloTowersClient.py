import FWCore.ParameterSet.Config as cms

def CaloTowersClient(**kwargs):
  mod = cms.EDProducer('CaloTowersClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
