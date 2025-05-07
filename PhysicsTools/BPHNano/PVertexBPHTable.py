import FWCore.ParameterSet.Config as cms

def PVertexBPHTable(*args, **kwargs):
  mod = cms.EDProducer('PVertexBPHTable',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
