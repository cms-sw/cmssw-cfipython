import FWCore.ParameterSet.Config as cms

def SiStripBadFiberBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripBadFiberBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
