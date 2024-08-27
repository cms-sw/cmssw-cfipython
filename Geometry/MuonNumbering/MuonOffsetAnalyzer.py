import FWCore.ParameterSet.Config as cms

def MuonOffsetAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('MuonOffsetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
