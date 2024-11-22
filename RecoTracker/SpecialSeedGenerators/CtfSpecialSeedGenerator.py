import FWCore.ParameterSet.Config as cms

def CtfSpecialSeedGenerator(*args, **kwargs):
  mod = cms.EDProducer('CtfSpecialSeedGenerator',
    SeedMomentum = cms.double(5),
    ErrorRescaling = cms.double(50),
    UseScintillatorsConstraint = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    SeedsFromPositiveY = cms.bool(True),
    SeedsFromNegativeY = cms.bool(False),
    CheckHitsAreOnDifferentLayers = cms.bool(False),
    SetMomentum = cms.bool(True),
    requireBOFF = cms.bool(False),
    maxSeeds = cms.int32(10000),
    doClusterCheck = cms.bool(True),
    MaxNumberOfStripClusters = cms.uint32(400000),
    ClusterCollectionLabel = cms.InputTag('siStripClusters'),
    MaxNumberOfPixelClusters = cms.uint32(40000),
    PixelClusterCollectionLabel = cms.InputTag('siPixelClusters'),
    cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
    DontCountDetsAboveNClusters = cms.uint32(0),
    Charges = cms.vint32(-1),
    RegionFactoryPSet = cms.PSet(
      ComponentName = cms.string('GlobalRegionProducer'),
      RegionPSet = cms.PSet()
    ),
    UpperScintillatorParameters = cms.PSet(
      LenghtInZ = cms.double(100),
      GlobalX = cms.double(0),
      GlobalY = cms.double(300),
      GlobalZ = cms.double(50),
      WidthInX = cms.double(100)
    ),
    LowerScintillatorParameters = cms.PSet(
      LenghtInZ = cms.double(100),
      GlobalX = cms.double(0),
      GlobalY = cms.double(-100),
      GlobalZ = cms.double(50),
      WidthInX = cms.double(100)
    ),
    OrderedHitsFactoryPSets = cms.VPSet(
      cms.PSet()
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
