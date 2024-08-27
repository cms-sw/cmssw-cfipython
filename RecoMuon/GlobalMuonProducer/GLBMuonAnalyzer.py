import FWCore.ParameterSet.Config as cms

def GLBMuonAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('GLBMuonAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
