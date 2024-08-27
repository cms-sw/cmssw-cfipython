import FWCore.ParameterSet.Config as cms

def L1GtPsbSetupTester(**kwargs):
  mod = cms.EDAnalyzer('L1GtPsbSetupTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
