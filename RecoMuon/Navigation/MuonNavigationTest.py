import FWCore.ParameterSet.Config as cms

def MuonNavigationTest(*args, **kwargs):
  mod = cms.EDAnalyzer('MuonNavigationTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
