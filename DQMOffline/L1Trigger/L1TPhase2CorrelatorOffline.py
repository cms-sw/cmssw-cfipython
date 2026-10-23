import FWCore.ParameterSet.Config as cms

def L1TPhase2CorrelatorOffline(*args, **kwargs):
  mod = cms.EDProducer('L1TPhase2CorrelatorOffline',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
