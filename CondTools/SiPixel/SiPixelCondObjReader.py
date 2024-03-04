import FWCore.ParameterSet.Config as cms

def SiPixelCondObjReader(**kwargs):
  mod = cms.EDAnalyzer('SiPixelCondObjReader',
    maxRangeDeadPixHist = cms.untracked.double(0.001),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
