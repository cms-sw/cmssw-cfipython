import FWCore.ParameterSet.Config as cms

def GoodVertexFilter(**kwargs):
  mod = cms.EDFilter('GoodVertexFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
