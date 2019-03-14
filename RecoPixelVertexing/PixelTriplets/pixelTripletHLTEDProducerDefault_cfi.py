import FWCore.ParameterSet.Config as cms

pixelTripletHLTEDProducerDefault = cms.EDProducer('PixelTripletHLTEDProducer',
  doublets = cms.InputTag('hitPairEDProducer'),
  produceSeedingHitSets = cms.bool(False),
  produceIntermediateHitTriplets = cms.bool(False),
  maxElement = cms.uint32(1000000),
  extraHitRPhitolerance = cms.double(0.032),
  extraHitRZtolerance = cms.double(0.037),
  useMultScattering = cms.bool(True),
  useBending = cms.bool(True),
  useFixedPreFiltering = cms.bool(False),
  phiPreFiltering = cms.double(0.3),
  SeedComparitorPSet = cms.PSet(
    ComponentName = cms.string('none')
  )
)
