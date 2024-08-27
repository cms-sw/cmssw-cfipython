import FWCore.ParameterSet.Config as cms

def CorrectedECALPFClusterProducer(**kwargs):
  mod = cms.EDProducer('CorrectedECALPFClusterProducer',
    minimumPSEnergy = cms.double(0),
    skipPS = cms.bool(False),
    inputPS = cms.InputTag('particleFlowClusterPS'),
    energyCorrector = cms.PSet(
      applyCrackCorrections = cms.bool(False),
      applyMVACorrections = cms.bool(False),
      srfAwareCorrection = cms.bool(False),
      setEnergyUncertainty = cms.bool(False),
      autoDetectBunchSpacing = cms.bool(True),
      bunchSpacing = cms.int32(25),
      maxPtForMVAEvaluation = cms.double(-99),
      recHitsEBLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
      recHitsEELabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
      ebSrFlagLabel = cms.InputTag('ecalDigis'),
      eeSrFlagLabel = cms.InputTag('ecalDigis')
    ),
    inputECAL = cms.InputTag('particleFlowClusterECALUncorrected'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
