import FWCore.ParameterSet.Config as cms

def SiStripO2OPedestals(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripO2OPedestals',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
