import FWCore.ParameterSet.Config as cms

def CandIsoDepositProducer(**kwargs):
  mod = cms.EDProducer('CandIsoDepositProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
