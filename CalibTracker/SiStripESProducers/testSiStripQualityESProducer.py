import FWCore.ParameterSet.Config as cms

def testSiStripQualityESProducer(**kwargs):
  mod = cms.EDAnalyzer('testSiStripQualityESProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
