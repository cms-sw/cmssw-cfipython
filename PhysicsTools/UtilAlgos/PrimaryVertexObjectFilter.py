import FWCore.ParameterSet.Config as cms

def PrimaryVertexObjectFilter(**kwargs):
  mod = cms.EDFilter('PrimaryVertexObjectFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
