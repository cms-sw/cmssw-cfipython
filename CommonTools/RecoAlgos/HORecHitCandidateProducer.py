import FWCore.ParameterSet.Config as cms

def HORecHitCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('HORecHitCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
