import FWCore.ParameterSet.Config as cms

def PATMuonSelector(*args, **kwargs):
  mod = cms.EDFilter('PATMuonSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod