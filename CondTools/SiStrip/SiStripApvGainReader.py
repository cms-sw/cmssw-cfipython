import FWCore.ParameterSet.Config as cms

def SiStripApvGainReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripApvGainReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
