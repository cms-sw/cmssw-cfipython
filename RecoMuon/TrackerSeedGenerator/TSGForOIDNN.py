import FWCore.ParameterSet.Config as cms

def TSGForOIDNN(**kwargs):
  mod = cms.EDProducer('TSGForOIDNN',
    src = cms.InputTag('hltL2Muons', 'UpdatedAtVtx'),
    layersToTry = cms.int32(2),
    fixedErrorRescaleFactorForHitless = cms.double(2),
    hitsToTry = cms.int32(1),
    MeasurementTrackerEvent = cms.InputTag('hltSiStripClusters'),
    estimator = cms.string('hltESPChi2MeasurementEstimator100'),
    maxEtaForTOB = cms.double(1.8),
    minEtaForTEC = cms.double(0.7),
    debug = cms.untracked.bool(False),
    maxSeeds = cms.uint32(20),
    maxHitlessSeeds = cms.uint32(5),
    maxHitSeeds = cms.uint32(1),
    propagatorName = cms.string('PropagatorWithMaterialParabolicMf'),
    maxHitlessSeedsIP = cms.uint32(5),
    maxHitlessSeedsMuS = cms.uint32(0),
    maxHitDoubletSeeds = cms.uint32(0),
    getStrategyFromDNN = cms.bool(False),
    useRegressor = cms.bool(False),
    dnnMetadataPath = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod