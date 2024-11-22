import FWCore.ParameterSet.Config as cms

def MuonPtFilter(*args, **kwargs):
  mod = cms.EDFilter('MuonPtFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
