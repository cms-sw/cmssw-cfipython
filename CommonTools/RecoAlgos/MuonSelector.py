import FWCore.ParameterSet.Config as cms

def MuonSelector(*args, **kwargs):
  mod = cms.EDFilter('MuonSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
