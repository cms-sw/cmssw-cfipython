import FWCore.ParameterSet.Config as cms

gemcscSegments = cms.EDProducer('GEMCSCSegmentProducer',
  inputObjectsGEM = cms.InputTag('gemRecHits'),
  inputObjectsCSC = cms.InputTag('cscSegments'),
  enableME21GE21 = cms.bool(False),
  algo_name = cms.string('GEMCSCSegAlgoRR'),
  algo_psets = cms.PSet(
    GEMCSCDebug = cms.untracked.bool(True),
    minHitsPerSegment = cms.uint32(2),
    preClustering = cms.bool(True),
    dXclusBoxMax = cms.double(1),
    dYclusBoxMax = cms.double(5),
    preClusteringUseChaining = cms.bool(True),
    dPhiChainBoxMax = cms.double(1),
    dThetaChainBoxMax = cms.double(0.02),
    dRChainBoxMax = cms.double(0.5),
    maxRecHitsInCluster = cms.int32(6)
  ),
  mightGet = cms.optional.untracked.vstring
)
