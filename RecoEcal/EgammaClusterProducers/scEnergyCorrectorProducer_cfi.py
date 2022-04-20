import FWCore.ParameterSet.Config as cms

scEnergyCorrectorProducer = cms.EDProducer('SCEnergyCorrectorProducer',
  correctorCfg = cms.PSet(
    isHLT = cms.bool(False),
    isPhaseII = cms.bool(False),
    regTrainedWithPS = cms.bool(False),
    applySigmaIetaIphiBug = cms.bool(False),
    ecalRecHitsEE = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
    ecalRecHitsEB = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    regressionKeyEB = cms.string('pfscecal_EBCorrection_offline_v2'),
    regressionKeyEE = cms.string('pfscecal_EECorrection_offline_v2'),
    uncertaintyKeyEB = cms.string('pfscecal_EBUncertainty_offline_v2'),
    uncertaintyKeyEE = cms.string('pfscecal_EEUncertainty_offline_v2'),
    regressionMinEB = cms.double(0.2),
    regressionMaxEB = cms.double(2),
    regressionMinEE = cms.double(0.2),
    regressionMaxEE = cms.double(2),
    uncertaintyMinEB = cms.double(0.0002),
    uncertaintyMaxEB = cms.double(0.5),
    uncertaintyMinEE = cms.double(0.0002),
    uncertaintyMaxEE = cms.double(0.5),
    vertexCollection = cms.InputTag('offlinePrimaryVertices'),
    eRecHitThreshold = cms.double(1),
    hgcalRecHits = cms.InputTag(''),
    hgcalCylinderR = cms.double(2.7999999523162842)
  ),
  writeFeatures = cms.bool(False),
  inputSCs = cms.InputTag('particleFlowSuperClusterECAL'),
  mightGet = cms.optional.untracked.vstring
)
