import FWCore.ParameterSet.Config as cms

def TwoBodyDecayConstraintProducer(**kwargs):
  mod = cms.EDProducer('TwoBodyDecayConstraintProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
