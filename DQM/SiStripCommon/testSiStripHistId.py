import FWCore.ParameterSet.Config as cms

def testSiStripHistId(**kwargs):
  mod = cms.EDAnalyzer('testSiStripHistId',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
