import FWCore.ParameterSet.Config as cms

def SiStripDeDx3DBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripDeDx3DBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
