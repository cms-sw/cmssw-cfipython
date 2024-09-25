import FWCore.ParameterSet.Config as cms

def testSiStripFedIdListReader(*args, **kwargs):
  mod = cms.EDAnalyzer('testSiStripFedIdListReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
