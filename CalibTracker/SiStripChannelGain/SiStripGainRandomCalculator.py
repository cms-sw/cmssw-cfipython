import FWCore.ParameterSet.Config as cms

def SiStripGainRandomCalculator(**kwargs):
  mod = cms.EDAnalyzer('SiStripGainRandomCalculator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
