import FWCore.ParameterSet.Config as cms

def PATMuonRefSelector(*args, **kwargs):
  mod = cms.EDFilter('PATMuonRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
