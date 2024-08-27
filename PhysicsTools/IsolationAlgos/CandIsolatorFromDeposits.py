import FWCore.ParameterSet.Config as cms

def CandIsolatorFromDeposits(**kwargs):
  mod = cms.EDProducer('CandIsolatorFromDeposits',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
