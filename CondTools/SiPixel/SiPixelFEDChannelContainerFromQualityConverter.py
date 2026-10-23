import FWCore.ParameterSet.Config as cms

def SiPixelFEDChannelContainerFromQualityConverter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelFEDChannelContainerFromQualityConverter',
    printDebug = cms.untracked.bool(False),
    removeEmptyPayloads = cms.untracked.bool(False),
    record = cms.string('SiPixelStatusScenariosRcd'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
