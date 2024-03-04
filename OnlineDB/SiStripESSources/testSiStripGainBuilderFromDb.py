import FWCore.ParameterSet.Config as cms

def testSiStripGainBuilderFromDb(**kwargs):
  mod = cms.EDAnalyzer('testSiStripGainBuilderFromDb',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
