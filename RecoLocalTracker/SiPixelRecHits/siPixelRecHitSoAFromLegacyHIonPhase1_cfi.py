import FWCore.ParameterSet.Config as cms

siPixelRecHitSoAFromLegacyHIonPhase1 = cms.EDProducer('SiPixelRecHitSoAFromLegacyHIonPhase1',
  beamSpot = cms.InputTag('offlineBeamSpot'),
  src = cms.InputTag('siPixelClustersPreSplitting'),
  CPE = cms.string('PixelCPEFastHIonPhase1'),
  convertToLegacy = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
