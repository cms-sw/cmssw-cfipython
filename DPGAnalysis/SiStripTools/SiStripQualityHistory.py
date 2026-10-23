import FWCore.ParameterSet.Config as cms

def SiStripQualityHistory(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripQualityHistory',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
