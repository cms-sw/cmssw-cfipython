import FWCore.ParameterSet.Config as cms

def HcalDetIdTableProducer(**kwargs):
  mod = cms.EDProducer('HcalDetIdTableProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
