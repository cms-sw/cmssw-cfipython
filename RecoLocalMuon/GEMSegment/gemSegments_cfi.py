import FWCore.ParameterSet.Config as cms

gemSegments = cms.EDProducer('GEMSegmentProducer',
  gemRecHitLabel = cms.InputTag('gemRecHits'),
  enableGE0 = cms.bool(True),
  enableGE12 = cms.bool(False),
  ge0_name = cms.string('GE0SegAlgoRU'),
  algo_name = cms.string('GEMSegmentAlgorithm'),
  ge0_pset = cms.PSet(
    allowWideSegments = cms.bool(True),
    doCollisions = cms.bool(True),
    maxChi2Additional = cms.double(100),
    maxChi2Prune = cms.double(50),
    maxChi2GoodSeg = cms.double(50),
    maxPhiSeeds = cms.double(0.001096605744),
    maxPhiAdditional = cms.double(0.001096605744),
    maxETASeeds = cms.double(0.1),
    maxTOFDiff = cms.double(25),
    requireCentralBX = cms.bool(True),
    minNumberOfHits = cms.uint32(4),
    maxNumberOfHits = cms.uint32(300),
    maxNumberOfHitsPerLayer = cms.uint32(100)
  ),
  algo_pset = cms.PSet(
    GEMDebug = cms.untracked.bool(False),
    minHitsPerSegment = cms.uint32(2),
    preClustering = cms.bool(True),
    dXclusBoxMax = cms.double(1),
    dYclusBoxMax = cms.double(5),
    preClusteringUseChaining = cms.bool(True),
    dPhiChainBoxMax = cms.double(0.02),
    dEtaChainBoxMax = cms.double(0.05),
    maxRecHitsInCluster = cms.int32(4),
    clusterOnlySameBXRecHits = cms.bool(True)
  ),
  mightGet = cms.optional.untracked.vstring
)
