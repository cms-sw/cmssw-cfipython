import FWCore.ParameterSet.Config as cms

def SiPixelCondObjReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelCondObjReader',
    maxRangeDeadPixHist = cms.untracked.double(0.001),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
