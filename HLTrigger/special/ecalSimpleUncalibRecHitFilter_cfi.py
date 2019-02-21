import FWCore.ParameterSet.Config as cms

ecalSimpleUncalibRecHitFilter = cms.EDFilter('EcalSimpleUncalibRecHitFilter',
  EcalUncalibRecHitCollection = cms.InputTag('ecalWeightUncalibRecHit', 'EcalUncalibRecHitsEB'),
  adcCut = cms.untracked.double(12),
  maskedChannels = cms.untracked.vint32()
)
