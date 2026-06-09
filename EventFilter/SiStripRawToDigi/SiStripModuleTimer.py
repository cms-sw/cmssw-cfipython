import FWCore.ParameterSet.Config as cms

def SiStripModuleTimer(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripModuleTimer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
