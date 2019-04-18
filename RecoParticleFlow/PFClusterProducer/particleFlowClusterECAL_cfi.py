import FWCore.ParameterSet.Config as cms

particleFlowClusterECAL = cms.EDProducer('CorrectedECALPFClusterProducer',
  minimumPSEnergy = cms.double(0),
  inputPS = cms.InputTag('particleFlowClusterPS'),
  energyCorrector = cms.PSet(
    applyCrackCorrections = cms.bool(False),
    applyMVACorrections = cms.bool(False),
    maxPtForMVAEvaluation = cms.double(-99),
    algoName = cms.string('PFClusterEMEnergyCorrector'),
    recHitsEBLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    recHitsEELabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
    verticesLabel = cms.InputTag('offlinePrimaryVertices'),
    autoDetectBunchSpacing = cms.bool(True),
    bunchSpacing = cms.int32(25)
  ),
  inputECAL = cms.InputTag('particleFlowClusterECALUncorrected')
)
