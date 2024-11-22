import FWCore.ParameterSet.Config as cms

def testSiStripEnumsAndStrings(*args, **kwargs):
  mod = cms.EDAnalyzer('testSiStripEnumsAndStrings',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
