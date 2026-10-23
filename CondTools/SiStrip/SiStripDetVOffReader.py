import FWCore.ParameterSet.Config as cms

def SiStripDetVOffReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripDetVOffReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
