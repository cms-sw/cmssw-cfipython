import FWCore.ParameterSet.Config as cms

def STAMuonAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('STAMuonAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
