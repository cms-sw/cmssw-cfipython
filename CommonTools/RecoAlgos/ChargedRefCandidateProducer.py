import FWCore.ParameterSet.Config as cms

def ChargedRefCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('ChargedRefCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
