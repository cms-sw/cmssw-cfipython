import FWCore.ParameterSet.Config as cms

def ClusterizerUnitTester(**kwargs):
  mod = cms.EDAnalyzer('ClusterizerUnitTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
