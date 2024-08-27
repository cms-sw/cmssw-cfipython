import FWCore.ParameterSet.Config as cms

def HcalTestNumberingTester(**kwargs):
  mod = cms.EDAnalyzer('HcalTestNumberingTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
