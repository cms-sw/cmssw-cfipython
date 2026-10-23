import FWCore.ParameterSet.Config as cms

def KFBasedPixelFitterProducer(*args, **kwargs):
  mod = cms.EDProducer('KFBasedPixelFitterProducer',
    useBeamSpotConstraint = cms.bool(True),
    beamSpotConstraint = cms.InputTag('offlineBeamSpot'),
    propagator = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    TTRHBuilder = cms.string('PixelTTRHBuilderWithoutAngle'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
