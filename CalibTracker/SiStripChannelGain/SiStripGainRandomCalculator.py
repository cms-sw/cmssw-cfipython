import FWCore.ParameterSet.Config as cms

def SiStripGainRandomCalculator(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripGainRandomCalculator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
