import FWCore.ParameterSet.Config as cms

def PatMuonEDAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PatMuonEDAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
