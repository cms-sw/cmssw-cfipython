import FWCore.ParameterSet.Config as cms

def MomentumConstraintProducer(**kwargs):
  mod = cms.EDProducer('MomentumConstraintProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
