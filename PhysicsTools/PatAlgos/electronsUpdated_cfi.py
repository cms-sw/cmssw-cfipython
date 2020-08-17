import FWCore.ParameterSet.Config as cms

electronsUpdated = cms.EDProducer('PATElectronUpdater',
  beamspot = cms.InputTag('offlineBeamSpot'),
  computeMiniIso = cms.bool(False),
  fixDxySign = cms.bool(False),
  pfCandsForMiniIso = cms.InputTag('packedPFCandidates')
)
