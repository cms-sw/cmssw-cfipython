import FWCore.ParameterSet.Config as cms

def SeedCreatorFromRegionConsecutiveHitsEDProducer(*args, **kwargs):
  mod = cms.EDProducer('SeedCreatorFromRegionConsecutiveHitsEDProducer',
    seedingHitSets = cms.InputTag('hitPairEDProducer'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    SeedMomentumForBOFF = cms.double(5),
    OriginTransverseErrorMultiplier = cms.double(1),
    MinOneOverPtError = cms.double(1),
    TTRHBuilder = cms.string('WithTrackAngle'),
    magneticField = cms.string('ParabolicMf'),
    forceKinematicWithRegionDirection = cms.bool(False),
    SeedComparitorPSet = cms.PSet(
      ComponentName = cms.string('none')
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
