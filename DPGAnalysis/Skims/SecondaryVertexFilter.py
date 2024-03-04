import FWCore.ParameterSet.Config as cms

def SecondaryVertexFilter(**kwargs):
  mod = cms.EDFilter('SecondaryVertexFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
