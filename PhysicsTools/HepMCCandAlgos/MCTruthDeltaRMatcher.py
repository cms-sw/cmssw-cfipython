import FWCore.ParameterSet.Config as cms

def MCTruthDeltaRMatcher(**kwargs):
  mod = cms.EDProducer('MCTruthDeltaRMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
