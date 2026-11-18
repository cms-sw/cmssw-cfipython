import FWCore.ParameterSet.Config as cms

def ClusterShapeHitFilterESProducer(*args, **kwargs):
  mod = cms.ESProducer('ClusterShapeHitFilterESProducer',
    pixelShapeLimitsLabel = cms.string(''),
    ComponentName = cms.string(''),
    isPhase2 = cms.bool(False),
    doPixelShapeCut = cms.bool(True),
    doStripShapeCut = cms.bool(True),
    clusterChargeCut = cms.PSet(
      value = cms.double(-1)
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
