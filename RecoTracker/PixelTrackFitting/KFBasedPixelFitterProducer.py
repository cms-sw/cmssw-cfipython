import FWCore.ParameterSet.Config as cms

def KFBasedPixelFitterProducer(**kwargs):
  mod = cms.EDProducer('KFBasedPixelFitterProducer',
    useBeamSpotConstraint = cms.bool(True),
    beamSpotConstraint = cms.InputTag('offlineBeamSpot'),
    propagator = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    TTRHBuilder = cms.string('PixelTTRHBuilderWithoutAngle'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
