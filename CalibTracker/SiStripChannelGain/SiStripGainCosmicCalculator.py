import FWCore.ParameterSet.Config as cms

def SiStripGainCosmicCalculator(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripGainCosmicCalculator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
