import FWCore.ParameterSet.Config as cms

def SimpleCosmicBONSeeder(*args, **kwargs):
  mod = cms.EDProducer('SimpleCosmicBONSeeder',
    TTRHBuilder = cms.string('WithTrackAngle'),
    ClusterCheckPSet = cms.PSet(
      doClusterCheck = cms.bool(True),
      MaxNumberOfStripClusters = cms.uint32(300),
      ClusterCollectionLabel = cms.InputTag('siStripClusters'),
      DontCountDetsAboveNClusters = cms.uint32(20),
      MaxNumberOfPixelClusters = cms.uint32(1000),
      PixelClusterCollectionLabel = cms.InputTag('siPixelClusters')
    ),
    maxTriplets = cms.int32(50000),
    maxSeeds = cms.int32(20000),
    RegionPSet = cms.PSet(
      originZPosition = cms.double(0),
      originRadius = cms.double(150),
      originHalfLength = cms.double(90),
      ptMin = cms.double(0.5),
      pMin = cms.double(1)
    ),
    TripletsSrc = cms.InputTag('simpleCosmicBONSeedingLayers'),
    TripletsDebugLevel = cms.untracked.uint32(0),
    seedOnMiddle = cms.bool(False),
    rescaleError = cms.double(1),
    ClusterChargeCheck = cms.PSet(
      checkCharge = cms.bool(False),
      matchedRecHitsUseAnd = cms.bool(True),
      Thresholds = cms.PSet(
        TIB = cms.int32(0),
        TID = cms.int32(0),
        TOB = cms.int32(0),
        TEC = cms.int32(0)
      )
    ),
    HitsPerModuleCheck = cms.PSet(
      checkHitsPerModule = cms.bool(True),
      Thresholds = cms.PSet(
        TIB = cms.int32(20),
        TID = cms.int32(20),
        TOB = cms.int32(20),
        TEC = cms.int32(20)
      )
    ),
    minimumGoodHitsInSeed = cms.int32(3),
    writeTriplets = cms.bool(False),
    helixDebugLevel = cms.untracked.uint32(0),
    seedDebugLevel = cms.untracked.uint32(0),
    PositiveYOnly = cms.bool(False),
    NegativeYOnly = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
