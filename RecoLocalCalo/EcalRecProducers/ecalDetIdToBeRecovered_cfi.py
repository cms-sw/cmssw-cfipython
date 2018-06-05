import FWCore.ParameterSet.Config as cms

ecalDetIdToBeRecovered = cms.EDProducer('EcalDetIdToBeRecoveredProducer',
  ebIntegrityChIdErrors = cms.InputTag('ecalDigis', 'EcalIntegrityChIdErrors'),
  ebDetIdToBeRecovered = cms.string('ebDetId'),
  integrityTTIdErrors = cms.InputTag('ecalDigis', 'EcalIntegrityTTIdErrors'),
  eeIntegrityGainErrors = cms.InputTag('ecalDigis', 'EcalIntegrityGainErrors'),
  ebFEToBeRecovered = cms.string('ebFE'),
  ebIntegrityGainErrors = cms.InputTag('ecalDigis', 'EcalIntegrityGainErrors'),
  eeDetIdToBeRecovered = cms.string('eeDetId'),
  eeIntegrityGainSwitchErrors = cms.InputTag('ecalDigis', 'EcalIntegrityGainSwitchErrors'),
  eeIntegrityChIdErrors = cms.InputTag('ecalDigis', 'EcalIntegrityChIdErrors'),
  ebIntegrityGainSwitchErrors = cms.InputTag('ecalDigis', 'EcalIntegrityGainSwitchErrors'),
  ebSrFlagCollection = cms.InputTag('ecalDigis'),
  eeFEToBeRecovered = cms.string('eeFE'),
  integrityBlockSizeErrors = cms.InputTag('ecalDigis', 'EcalIntegrityBlockSizeErrors'),
  eeSrFlagCollection = cms.InputTag('ecalDigis')
)
