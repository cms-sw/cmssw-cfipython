import FWCore.ParameterSet.Config as cms

def MuonGeometryConstantsTester(**kwargs):
  mod = cms.EDAnalyzer('MuonGeometryConstantsTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
