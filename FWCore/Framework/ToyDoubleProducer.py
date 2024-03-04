import FWCore.ParameterSet.Config as cms

def ToyDoubleProducer(**kwargs):
  mod = cms.EDProducer('ToyDoubleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
