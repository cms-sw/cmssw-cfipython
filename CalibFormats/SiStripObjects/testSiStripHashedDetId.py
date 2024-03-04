import FWCore.ParameterSet.Config as cms

def testSiStripHashedDetId(**kwargs):
  mod = cms.EDAnalyzer('testSiStripHashedDetId',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
