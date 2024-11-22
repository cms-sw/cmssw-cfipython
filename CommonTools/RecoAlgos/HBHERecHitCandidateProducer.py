import FWCore.ParameterSet.Config as cms

def HBHERecHitCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('HBHERecHitCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
