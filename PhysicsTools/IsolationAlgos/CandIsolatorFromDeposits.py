import FWCore.ParameterSet.Config as cms

def CandIsolatorFromDeposits(*args, **kwargs):
  mod = cms.EDProducer('CandIsolatorFromDeposits',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
