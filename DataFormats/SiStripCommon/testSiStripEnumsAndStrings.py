import FWCore.ParameterSet.Config as cms

def testSiStripEnumsAndStrings(**kwargs):
  mod = cms.EDAnalyzer('testSiStripEnumsAndStrings',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
