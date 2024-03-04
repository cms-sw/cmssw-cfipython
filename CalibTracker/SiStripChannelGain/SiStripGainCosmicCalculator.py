import FWCore.ParameterSet.Config as cms

def SiStripGainCosmicCalculator(**kwargs):
  mod = cms.EDAnalyzer('SiStripGainCosmicCalculator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
