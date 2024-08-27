import FWCore.ParameterSet.Config as cms

def TwoBodyDecayMomConstraintProducer(**kwargs):
  mod = cms.EDProducer('TwoBodyDecayMomConstraintProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
