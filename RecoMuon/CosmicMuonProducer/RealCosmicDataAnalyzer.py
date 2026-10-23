import FWCore.ParameterSet.Config as cms

def RealCosmicDataAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('RealCosmicDataAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
