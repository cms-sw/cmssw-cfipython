import FWCore.ParameterSet.Config as cms

def HLTTauPostProcessor(*args, **kwargs):
  mod = cms.EDProducer('HLTTauPostProcessor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
