import FWCore.ParameterSet.Config as cms

def MuonSeedParametrization(*args, **kwargs):
  mod = cms.EDAnalyzer('MuonSeedParametrization',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
