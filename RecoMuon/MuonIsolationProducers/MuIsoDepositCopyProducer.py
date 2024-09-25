import FWCore.ParameterSet.Config as cms

def MuIsoDepositCopyProducer(*args, **kwargs):
  mod = cms.EDProducer('MuIsoDepositCopyProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
