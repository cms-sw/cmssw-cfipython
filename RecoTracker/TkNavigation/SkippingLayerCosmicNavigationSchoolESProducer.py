import FWCore.ParameterSet.Config as cms

def SkippingLayerCosmicNavigationSchoolESProducer(*args, **kwargs):
  mod = cms.ESProducer('SkippingLayerCosmicNavigationSchoolESProducer',
    ComponentName = cms.required.string,
    noPXB = cms.required.bool,
    noPXF = cms.required.bool,
    noTIB = cms.required.bool,
    noTID = cms.required.bool,
    noTOB = cms.required.bool,
    noTEC = cms.required.bool,
    selfSearch = cms.required.bool,
    allSelf = cms.required.bool,
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
