import FWCore.ParameterSet.Config as cms

def BestMassZArbitrationProducer(**kwargs):
  mod = cms.EDProducer('BestMassZArbitrationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
