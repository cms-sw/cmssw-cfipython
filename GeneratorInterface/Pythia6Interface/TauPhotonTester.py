import FWCore.ParameterSet.Config as cms

def TauPhotonTester(*args, **kwargs):
  mod = cms.EDAnalyzer('TauPhotonTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
