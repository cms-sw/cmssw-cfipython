import FWCore.ParameterSet.Config as cms

def MCTruthDeltaRViewMatcher(**kwargs):
  mod = cms.EDProducer('MCTruthDeltaRViewMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
