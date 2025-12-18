import FWCore.ParameterSet.Config as cms

def MCTruthDeltaRMatcher(*args, **kwargs):
  mod = cms.EDProducer('MCTruthDeltaRMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
