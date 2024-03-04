import FWCore.ParameterSet.Config as cms

def TestBXVectorRefProducer(**kwargs):
  mod = cms.EDProducer('TestBXVectorRefProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
