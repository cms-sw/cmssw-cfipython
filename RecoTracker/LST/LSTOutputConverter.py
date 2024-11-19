import FWCore.ParameterSet.Config as cms

def LSTOutputConverter(*args, **kwargs):
  mod = cms.EDProducer('LSTOutputConverter',
    lstOutput = cms.InputTag('lstProducer'),
    phase2OTHits = cms.InputTag('lstPhase2OTHitsInputProducer'),
    lstPixelSeeds = cms.InputTag('lstPixelSeedInputProducer'),
    includeT5s = cms.bool(True),
    includeNonpLSTSs = cms.bool(False),
    propagatorAlong = cms.ESInputTag('', 'PropagatorWithMaterial'),
    propagatorOpposite = cms.ESInputTag('', 'PropagatorWithMaterialOpposite'),
    SeedCreatorPSet = cms.PSet(
      ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
      propagator = cms.string('PropagatorWithMaterial'),
      SeedMomentumForBOFF = cms.double(5),
      OriginTransverseErrorMultiplier = cms.double(1),
      MinOneOverPtError = cms.double(1),
      magneticField = cms.string(''),
      TTRHBuilder = cms.string('WithTrackAngle'),
      forceKinematicWithRegionDirection = cms.bool(False)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
