import FWCore.ParameterSet.Config as cms

def MuonVIDCITKAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('MuonVIDCITKAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
