import FWCore.ParameterSet.Config as cms

def HFRecHitCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('HFRecHitCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
