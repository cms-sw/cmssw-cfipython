import FWCore.ParameterSet.Config as cms

pixelTripletLargeTipEDProducerDefault = cms.EDProducer('PixelTripletLargeTipEDProducer',
  doublets = cms.InputTag('hitPairEDProducer'),
  produceSeedingHitSets = cms.bool(False),
  produceIntermediateHitTriplets = cms.bool(False),
  maxElement = cms.uint32(1000000),
  extraHitRPhitolerance = cms.double(0),
  extraHitRZtolerance = cms.double(0),
  useMultScattering = cms.bool(True),
  useBending = cms.bool(True),
  useFixedPreFiltering = cms.bool(False),
  phiPreFiltering = cms.double(0.3)
)
