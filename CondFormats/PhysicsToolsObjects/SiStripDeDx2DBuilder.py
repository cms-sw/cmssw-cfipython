import FWCore.ParameterSet.Config as cms

def SiStripDeDx2DBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripDeDx2DBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
