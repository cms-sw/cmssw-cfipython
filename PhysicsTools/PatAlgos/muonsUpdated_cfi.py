import FWCore.ParameterSet.Config as cms

muonsUpdated = cms.EDProducer('PATMuonUpdater',
  computeMiniIso = cms.bool(False),
  pfCandsForMiniIso = cms.InputTag('packedPFCandidates'),
  recomputeMuonBasicSelectors = cms.bool(False)
)
