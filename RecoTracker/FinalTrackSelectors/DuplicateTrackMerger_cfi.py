import FWCore.ParameterSet.Config as cms

DuplicateTrackMerger = cms.EDProducer('DuplicateTrackMerger',
  source = cms.InputTag(''),
  minDeltaR3d = cms.double(-4),
  minBDTG = cms.double(-0.1),
  minpT = cms.double(0.2),
  minP = cms.double(0.4),
  maxDCA = cms.double(30),
  maxDPhi = cms.double(0.3),
  maxDLambda = cms.double(0.3),
  maxDdsz = cms.double(10),
  maxDdxy = cms.double(10),
  maxDQoP = cms.double(0.25),
  overlapCheckMaxHits = cms.uint32(4),
  overlapCheckMaxMissingLayers = cms.uint32(1),
  overlapCheckMinCosT = cms.double(0.99),
  forestLabel = cms.string('MVADuplicate'),
  GBRForestFileName = cms.string(''),
  useInnermostState = cms.bool(True),
  ttrhBuilderName = cms.string('WithAngleAndTemplate'),
  propagatorName = cms.string('PropagatorWithMaterial'),
  chi2EstimatorName = cms.string('DuplicateTrackMergerChi2Est')
)
