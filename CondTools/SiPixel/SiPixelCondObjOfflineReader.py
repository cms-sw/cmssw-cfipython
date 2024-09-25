import FWCore.ParameterSet.Config as cms

def SiPixelCondObjOfflineReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelCondObjOfflineReader',
    useSimRcd = cms.bool(False),
    maxRangeDeadPixHist = cms.untracked.double(0.001),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
