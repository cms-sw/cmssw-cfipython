import FWCore.ParameterSet.Config as cms

def SiStripThresholdReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripThresholdReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
