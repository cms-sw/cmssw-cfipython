import FWCore.ParameterSet.Config as cms

hiFJGridEmptyAreaCalculator = cms.EDProducer('HiFJGridEmptyAreaCalculator',
  jetSource = cms.InputTag('kt4PFJets'),
  CentralityBinSrc = cms.InputTag('centralityBin'),
  mapEtaEdges = cms.InputTag('mapEtaEdges'),
  mapToRho = cms.InputTag('mapToRho'),
  mapToRhoM = cms.InputTag('mapToRhoM'),
  pfCandSource = cms.InputTag('particleFlow'),
  gridWidth = cms.double(0.05),
  bandWidth = cms.double(0.2),
  doCentrality = cms.bool(True),
  hiBinCut = cms.int32(100),
  keepGridInfo = cms.bool(False)
)
