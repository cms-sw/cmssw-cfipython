import FWCore.ParameterSet.Config as cms

def SiPixelFEDChannelContainerFromQualityConverter(**kwargs):
  mod = cms.EDAnalyzer('SiPixelFEDChannelContainerFromQualityConverter',
    printDebug = cms.untracked.bool(False),
    removeEmptyPayloads = cms.untracked.bool(False),
    record = cms.string('SiPixelStatusScenariosRcd'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
