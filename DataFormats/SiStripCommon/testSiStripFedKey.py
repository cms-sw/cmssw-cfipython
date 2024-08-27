import FWCore.ParameterSet.Config as cms

def testSiStripFedKey(**kwargs):
  mod = cms.EDAnalyzer('testSiStripFedKey',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
