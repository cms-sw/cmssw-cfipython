import FWCore.ParameterSet.Config as cms

def testSiStripGainBuilderFromDb(*args, **kwargs):
  mod = cms.EDAnalyzer('testSiStripGainBuilderFromDb',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
