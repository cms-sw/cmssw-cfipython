import FWCore.ParameterSet.Config as cms

def MCTruthDeltaRMatcherNew(*args, **kwargs):
  mod = cms.EDProducer('MCTruthDeltaRMatcherNew',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
