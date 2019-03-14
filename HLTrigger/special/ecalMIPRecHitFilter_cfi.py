import FWCore.ParameterSet.Config as cms

ecalMIPRecHitFilter = cms.EDFilter('EcalMIPRecHitFilter',
  EcalRecHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
  AmpMinSeed = cms.untracked.double(0.045),
  AmpMin2 = cms.untracked.double(0.045),
  SingleAmpMin = cms.untracked.double(0.108),
  maskedChannels = cms.untracked.vint32(),
  side = cms.untracked.int32(3)
)
