import FWCore.ParameterSet.Config as cms

def SiStripSpyDisplayModule(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripSpyDisplayModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
