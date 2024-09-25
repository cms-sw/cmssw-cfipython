import FWCore.ParameterSet.Config as cms

def MuonVIDCITKAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('MuonVIDCITKAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
