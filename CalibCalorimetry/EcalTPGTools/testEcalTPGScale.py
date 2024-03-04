import FWCore.ParameterSet.Config as cms

def testEcalTPGScale(**kwargs):
  mod = cms.EDAnalyzer('testEcalTPGScale',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
