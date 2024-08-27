import FWCore.ParameterSet.Config as cms

def MCPdgIndexFilter(**kwargs):
  mod = cms.EDFilter('MCPdgIndexFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
