import FWCore.ParameterSet.Config as cms

def ZDCRecHitCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('ZDCRecHitCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
