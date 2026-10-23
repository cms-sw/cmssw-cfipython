import FWCore.ParameterSet.Config as cms

def SiPixelBadModuleByHandBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelBadModuleByHandBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
