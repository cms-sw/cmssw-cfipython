import FWCore.ParameterSet.Config as cms

def HcalTopologyTester(**kwargs):
  mod = cms.EDAnalyzer('HcalTopologyTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
