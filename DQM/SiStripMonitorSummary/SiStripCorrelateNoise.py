import FWCore.ParameterSet.Config as cms

def SiStripCorrelateNoise(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripCorrelateNoise',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
