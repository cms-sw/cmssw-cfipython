import FWCore.ParameterSet.Config as cms

def GlobalDigisProducer(**kwargs):
  mod = cms.EDProducer('GlobalDigisProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
