import FWCore.ParameterSet.Config as cms

def MuonGeometryArrange(**kwargs):
  mod = cms.EDAnalyzer('MuonGeometryArrange',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
