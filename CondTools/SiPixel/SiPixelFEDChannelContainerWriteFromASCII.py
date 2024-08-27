import FWCore.ParameterSet.Config as cms

def SiPixelFEDChannelContainerWriteFromASCII(**kwargs):
  mod = cms.EDAnalyzer('SiPixelFEDChannelContainerWriteFromASCII',
    printDebug = cms.untracked.bool(True),
    addDefault = cms.untracked.bool(True),
    snapshots = cms.string(''),
    record = cms.string('SiPixelStatusScenariosRcd'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
