import FWCore.ParameterSet.Config as cms

SeedGeneratorFromProtoTracksEDProducer = cms.EDProducer('SeedGeneratorFromProtoTracksEDProducer',
  InputCollection = cms.InputTag('pixelTracks'),
  InputVertexCollection = cms.InputTag(''),
  originHalfLength = cms.double(1000000000),
  originRadius = cms.double(1000000000),
  useProtoTrackKinematics = cms.bool(False),
  useEventsWithNoVertex = cms.bool(True),
  TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
  usePV = cms.bool(False),
  SeedCreatorPSet = cms.PSet(
    ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
    propagator = cms.string('PropagatorWithMaterial'),
    SeedMomentumForBOFF = cms.double(5),
    OriginTransverseErrorMultiplier = cms.double(1),
    MinOneOverPtError = cms.double(1),
    magneticField = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False)
  )
)
