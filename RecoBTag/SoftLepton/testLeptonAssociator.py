import FWCore.ParameterSet.Config as cms

def testLeptonAssociator(**kwargs):
  mod = cms.EDAnalyzer('testLeptonAssociator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
