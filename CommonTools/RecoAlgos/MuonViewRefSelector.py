import FWCore.ParameterSet.Config as cms

def MuonViewRefSelector(*args, **kwargs):
  mod = cms.EDFilter('MuonViewRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
