import FWCore.ParameterSet.Config as cms

def SiStripCorrelateBadStripAndNoise(**kwargs):
  mod = cms.EDAnalyzer('SiStripCorrelateBadStripAndNoise',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
