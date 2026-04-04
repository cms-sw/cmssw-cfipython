import FWCore.ParameterSet.Config as cms

def TestBXVectorRefProducer(*args, **kwargs):
  mod = cms.EDProducer('TestBXVectorRefProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
