import FWCore.ParameterSet.Config as cms

def testSiStripKey(**kwargs):
  mod = cms.EDAnalyzer('testSiStripKey',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
