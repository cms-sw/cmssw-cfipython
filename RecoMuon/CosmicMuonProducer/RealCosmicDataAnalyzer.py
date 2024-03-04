import FWCore.ParameterSet.Config as cms

def RealCosmicDataAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('RealCosmicDataAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
