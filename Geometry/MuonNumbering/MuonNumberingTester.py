import FWCore.ParameterSet.Config as cms

def MuonNumberingTester(**kwargs):
  mod = cms.EDAnalyzer('MuonNumberingTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
