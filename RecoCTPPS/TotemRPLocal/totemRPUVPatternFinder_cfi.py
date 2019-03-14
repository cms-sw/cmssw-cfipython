import FWCore.ParameterSet.Config as cms

totemRPUVPatternFinder = cms.EDProducer('TotemRPUVPatternFinder',
  tagRecHit = cms.InputTag('totemRPRecHitProducer'),
  verbosity = cms.untracked.uint32(0),
  maxHitsPerPlaneToSearch = cms.uint32(5),
  minPlanesPerProjectionToSearch = cms.uint32(3),
  clusterSize_a = cms.double(0.02),
  clusterSize_b = cms.double(0.3),
  threshold = cms.double(2.99),
  minPlanesPerProjectionToFit = cms.uint32(3),
  allowAmbiguousCombination = cms.bool(False),
  max_a_toFit = cms.double(10),
  exceptionalSettings = cms.VPSet(
  )
)
