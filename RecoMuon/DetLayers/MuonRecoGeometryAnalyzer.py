import FWCore.ParameterSet.Config as cms

def MuonRecoGeometryAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('MuonRecoGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
