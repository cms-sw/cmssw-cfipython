import FWCore.ParameterSet.Config as cms

kfBasedPixelFitter = cms.EDProducer('KFBasedPixelFitterProducer',
  useBeamSpotConstraint = cms.bool(True),
  beamSpotConstraint = cms.InputTag('offlineBeamSpot'),
  propagator = cms.string('PropagatorWithMaterial'),
  propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
  TTRHBuilder = cms.string('PixelTTRHBuilderWithoutAngle')
)
