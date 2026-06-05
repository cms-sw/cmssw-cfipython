import FWCore.ParameterSet.Config as cms

def TwoBodyDecayConstraintProducer(*args, **kwargs):
  mod = cms.EDProducer('TwoBodyDecayConstraintProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
