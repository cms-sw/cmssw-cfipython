import FWCore.ParameterSet.Config as cms

def SiPixelCondObjForHLTBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelCondObjForHLTBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
