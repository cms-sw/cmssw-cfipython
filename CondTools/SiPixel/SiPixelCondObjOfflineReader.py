import FWCore.ParameterSet.Config as cms

def SiPixelCondObjOfflineReader(**kwargs):
  mod = cms.EDAnalyzer('SiPixelCondObjOfflineReader',
    useSimRcd = cms.bool(False),
    maxRangeDeadPixHist = cms.untracked.double(0.001),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
