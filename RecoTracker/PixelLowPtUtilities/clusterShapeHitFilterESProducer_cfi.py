import FWCore.ParameterSet.Config as cms

clusterShapeHitFilterESProducer = cms.ESProducer('ClusterShapeHitFilterESProducer',
  PixelShapeFile = cms.string('RecoTracker/PixelLowPtUtilities/data/pixelShapePhase0.par'),
  PixelShapeFileL1 = cms.string('RecoTracker/PixelLowPtUtilities/data/pixelShapePhase0.par'),
  ComponentName = cms.string(''),
  isPhase2 = cms.bool(False),
  doPixelShapeCut = cms.bool(True),
  doStripShapeCut = cms.bool(True),
  clusterChargeCut = cms.PSet(
    value = cms.double(-1)
  ),
  appendToDataLabel = cms.string('')
)