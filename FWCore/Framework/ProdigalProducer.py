import FWCore.ParameterSet.Config as cms

def ProdigalProducer(**kwargs):
  mod = cms.EDProducer('ProdigalProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
