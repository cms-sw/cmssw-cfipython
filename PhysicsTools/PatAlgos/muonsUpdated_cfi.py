import FWCore.ParameterSet.Config as cms

muonsUpdated = cms.EDProducer('PATMuonUpdater',
  beamspot = cms.InputTag('offlineBeamSpot'),
  computeMiniIso = cms.bool(False),
  fixDxySign = cms.bool(False),
  pfCandsForMiniIso = cms.InputTag('packedPFCandidates'),
  recomputeMuonBasicSelectors = cms.bool(False)
)
