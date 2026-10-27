import FWCore.ParameterSet.Config as cms

def SiPixelClusterShapeLimitsReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelClusterShapeLimitsReader',
    label = cms.string(''),
    outputFile = cms.untracked.string(''),
    printDebug = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
