import FWCore.ParameterSet.Config as cms

def SiPixelFEDChannelContainerWriteFromASCII(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelFEDChannelContainerWriteFromASCII',
    printDebug = cms.untracked.bool(True),
    addDefault = cms.untracked.bool(True),
    snapshots = cms.string(''),
    record = cms.string('SiPixelStatusScenariosRcd'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
