import FWCore.ParameterSet.Config as cms

siPixelRecHitSoAFromLegacyPhase1 = cms.EDProducer('SiPixelRecHitSoAFromLegacyPhase1',
  beamSpot = cms.InputTag('offlineBeamSpot'),
  src = cms.InputTag('siPixelClustersPreSplitting'),
  CPE = cms.string('PixelCPEFast'),
  convertToLegacy = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
