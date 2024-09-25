import FWCore.ParameterSet.Config as cms

def MuonRecoGeometryAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('MuonRecoGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
