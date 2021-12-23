import FWCore.ParameterSet.Config as cms

siPixelRecHitSoAFromLegacy = cms.EDProducer('SiPixelRecHitSoAFromLegacy',
  beamSpot = cms.InputTag('offlineBeamSpot'),
  src = cms.InputTag('siPixelClustersPreSplitting'),
  CPE = cms.string('PixelCPEFast'),
  convertToLegacy = cms.bool(False),
  isPhase2 = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
