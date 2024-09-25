import FWCore.ParameterSet.Config as cms

def testSiStripHistoTitle(*args, **kwargs):
  mod = cms.EDAnalyzer('testSiStripHistoTitle',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
