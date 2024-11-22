import FWCore.ParameterSet.Config as cms

def ConcreteChargedCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('ConcreteChargedCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
