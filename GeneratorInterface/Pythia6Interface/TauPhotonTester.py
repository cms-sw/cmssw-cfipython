import FWCore.ParameterSet.Config as cms

def TauPhotonTester(**kwargs):
  mod = cms.EDAnalyzer('TauPhotonTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
