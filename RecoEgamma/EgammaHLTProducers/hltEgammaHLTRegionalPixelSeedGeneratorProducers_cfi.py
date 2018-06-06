import FWCore.ParameterSet.Config as cms

hltEgammaHLTRegionalPixelSeedGeneratorProducers = cms.EDProducer('EgammaHLTRegionalPixelSeedGeneratorProducers',
  ptMin = cms.double(1.5),
  vertexZ = cms.double(0),
  originRadius = cms.double(0.02),
  originHalfLength = cms.double(15),
  deltaEtaRegion = cms.double(0.3),
  deltaPhiRegion = cms.double(0.3),
  candTag = cms.InputTag('hltL1SeededRecoEcalCandidate'),
  candTagEle = cms.InputTag('pixelMatchElectrons'),
  BSProducer = cms.InputTag('hltOnlineBeamSpot'),
  UseZInVertex = cms.bool(False),
  TTRHBuilder = cms.string('WithTrackAngle'),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string('StandardHitPairGenerator'),
    SeedingLayers = cms.InputTag('PixelLayerPairs'),
    maxElement = cms.uint32(0)
  )
)
