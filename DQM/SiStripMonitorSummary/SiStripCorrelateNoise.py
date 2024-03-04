import FWCore.ParameterSet.Config as cms

def SiStripCorrelateNoise(**kwargs):
  mod = cms.EDAnalyzer('SiStripCorrelateNoise',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
