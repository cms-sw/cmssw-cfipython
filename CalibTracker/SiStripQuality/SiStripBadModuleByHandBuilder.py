import FWCore.ParameterSet.Config as cms

def SiStripBadModuleByHandBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripBadModuleByHandBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
