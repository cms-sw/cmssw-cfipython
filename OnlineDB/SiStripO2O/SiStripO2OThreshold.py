import FWCore.ParameterSet.Config as cms

def SiStripO2OThreshold(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripO2OThreshold',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
