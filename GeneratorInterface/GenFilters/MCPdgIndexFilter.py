import FWCore.ParameterSet.Config as cms

def MCPdgIndexFilter(*args, **kwargs):
  mod = cms.EDFilter('MCPdgIndexFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
