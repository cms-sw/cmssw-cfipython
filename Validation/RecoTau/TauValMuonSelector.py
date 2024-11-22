import FWCore.ParameterSet.Config as cms

def TauValMuonSelector(*args, **kwargs):
  mod = cms.EDFilter('TauValMuonSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
