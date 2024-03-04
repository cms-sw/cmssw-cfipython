import FWCore.ParameterSet.Config as cms

def CaloTowersValidation(**kwargs):
  mod = cms.EDProducer('CaloTowersValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
