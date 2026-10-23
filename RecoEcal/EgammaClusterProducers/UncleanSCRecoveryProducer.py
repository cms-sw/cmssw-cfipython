import FWCore.ParameterSet.Config as cms

def UncleanSCRecoveryProducer(*args, **kwargs):
  mod = cms.EDProducer('UncleanSCRecoveryProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
