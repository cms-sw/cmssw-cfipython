import FWCore.ParameterSet.Config as cms

def HLTMuonPtFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTMuonPtFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
