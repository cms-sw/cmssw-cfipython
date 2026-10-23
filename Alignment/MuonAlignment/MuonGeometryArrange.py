import FWCore.ParameterSet.Config as cms

def MuonGeometryArrange(*args, **kwargs):
  mod = cms.EDAnalyzer('MuonGeometryArrange',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
