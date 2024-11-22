import FWCore.ParameterSet.Config as cms

def ConcreteEcalCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('ConcreteEcalCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
