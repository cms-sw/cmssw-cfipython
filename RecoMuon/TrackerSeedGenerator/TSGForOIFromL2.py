import FWCore.ParameterSet.Config as cms

def TSGForOIFromL2(**kwargs):
  mod = cms.EDProducer('TSGForOIFromL2',
    src = cms.InputTag('hltL2Muons', 'UpdatedAtVtx'),
    layersToTry = cms.int32(2),
    fixedErrorRescaleFactorForHitless = cms.double(2),
    hitsToTry = cms.int32(1),
    adjustErrorsDynamicallyForHits = cms.bool(False),
    adjustErrorsDynamicallyForHitless = cms.bool(True),
    MeasurementTrackerEvent = cms.InputTag('hltSiStripClusters'),
    UseHitLessSeeds = cms.bool(True),
    estimator = cms.string('hltESPChi2MeasurementEstimator100'),
    maxEtaForTOB = cms.double(1.8),
    minEtaForTEC = cms.double(0.7),
    debug = cms.untracked.bool(False),
    fixedErrorRescaleFactorForHits = cms.double(1),
    maxSeeds = cms.uint32(20),
    maxHitlessSeeds = cms.uint32(5),
    maxHitSeeds = cms.uint32(1),
    numL2ValidHitsCutAllEta = cms.uint32(20),
    numL2ValidHitsCutAllEndcap = cms.uint32(30),
    pT1 = cms.double(13),
    pT2 = cms.double(30),
    pT3 = cms.double(70),
    eta1 = cms.double(0.2),
    eta2 = cms.double(0.3),
    eta3 = cms.double(1),
    eta4 = cms.double(1.2),
    eta5 = cms.double(1.6),
    eta6 = cms.double(1.4),
    eta7 = cms.double(2.1),
    SF1 = cms.double(3),
    SF2 = cms.double(4),
    SF3 = cms.double(5),
    SF4 = cms.double(7),
    SF5 = cms.double(10),
    SF6 = cms.double(2),
    SFHld = cms.double(2),
    SFHd = cms.double(4),
    tsosDiff1 = cms.double(0.2),
    tsosDiff2 = cms.double(0.02),
    displacedReco = cms.bool(False),
    propagatorName = cms.string('PropagatorWithMaterialParabolicMf'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
