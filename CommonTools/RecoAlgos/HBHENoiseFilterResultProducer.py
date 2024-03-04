import FWCore.ParameterSet.Config as cms

def HBHENoiseFilterResultProducer(**kwargs):
  mod = cms.EDProducer('HBHENoiseFilterResultProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
