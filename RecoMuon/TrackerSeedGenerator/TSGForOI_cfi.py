import FWCore.ParameterSet.Config as cms

TSGForOI = cms.EDProducer('TSGForOI',
  src = cms.InputTag('hltL2Muons', 'UpdatedAtVtx'),
  layersToTry = cms.int32(1),
  fixedErrorRescaleFactorForHitless = cms.double(2),
  hitsToTry = cms.int32(1),
  adjustErrorsDynamicallyForHits = cms.bool(False),
  adjustErrorsDynamicallyForHitless = cms.bool(False),
  MeasurementTrackerEvent = cms.InputTag('hltSiStripClusters'),
  UseHitLessSeeds = cms.bool(True),
  UseStereoLayersInTEC = cms.bool(False),
  estimator = cms.string('hltESPChi2MeasurementEstimator100'),
  maxEtaForTOB = cms.double(1.2),
  minEtaForTEC = cms.double(0.8),
  debug = cms.untracked.bool(True),
  fixedErrorRescaleFactorForHits = cms.double(2),
  maxSeeds = cms.uint32(1),
  pT1 = cms.double(13),
  pT2 = cms.double(30),
  pT3 = cms.double(70),
  eta1 = cms.double(1),
  eta2 = cms.double(1.4),
  SF1 = cms.double(3),
  SF2 = cms.double(4),
  SF3 = cms.double(5),
  SF4 = cms.double(7),
  SF5 = cms.double(10),
  tsosDiff = cms.double(0.03),
  propagatorName = cms.string('PropagatorWithMaterial'),
  mightGet = cms.optional.untracked.vstring
)
