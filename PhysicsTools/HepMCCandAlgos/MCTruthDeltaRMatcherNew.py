import FWCore.ParameterSet.Config as cms

def MCTruthDeltaRMatcherNew(**kwargs):
  mod = cms.EDProducer('MCTruthDeltaRMatcherNew',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
