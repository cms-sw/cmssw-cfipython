import FWCore.ParameterSet.Config as cms

def testMuonAssociator(**kwargs):
  mod = cms.EDAnalyzer('testMuonAssociator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
