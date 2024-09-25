import FWCore.ParameterSet.Config as cms

def ConcreteChargedRefCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('ConcreteChargedRefCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
