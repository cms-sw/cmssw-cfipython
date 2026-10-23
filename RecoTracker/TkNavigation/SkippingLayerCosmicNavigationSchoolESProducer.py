import FWCore.ParameterSet.Config as cms

def SkippingLayerCosmicNavigationSchoolESProducer(*args, **kwargs):
  mod = cms.ESProducer('SkippingLayerCosmicNavigationSchoolESProducer',
    ComponentName = cms.string('CosmicNavigationSchool'),
    noPXB = cms.bool(False),
    noPXF = cms.bool(False),
    noTIB = cms.bool(False),
    noTID = cms.bool(False),
    noTOB = cms.bool(False),
    noTEC = cms.bool(False),
    selfSearch = cms.bool(True),
    allSelf = cms.bool(True),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
