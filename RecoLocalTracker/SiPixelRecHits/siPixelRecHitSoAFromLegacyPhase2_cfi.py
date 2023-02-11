import FWCore.ParameterSet.Config as cms

siPixelRecHitSoAFromLegacyPhase2 = cms.EDProducer('SiPixelRecHitSoAFromLegacyPhase2',
  beamSpot = cms.InputTag('offlineBeamSpot'),
  src = cms.InputTag('siPixelClustersPreSplitting'),
  CPE = cms.string('PixelCPEFastPhase2'),
  convertToLegacy = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
