import FWCore.ParameterSet.Config as cms

def MomentumConstraintProducer(*args, **kwargs):
  mod = cms.EDProducer('MomentumConstraintProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
