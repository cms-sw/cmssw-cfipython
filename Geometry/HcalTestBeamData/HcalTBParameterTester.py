import FWCore.ParameterSet.Config as cms

def HcalTBParameterTester(**kwargs):
  mod = cms.EDAnalyzer('HcalTBParameterTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
