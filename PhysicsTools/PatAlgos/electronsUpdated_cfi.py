import FWCore.ParameterSet.Config as cms

electronsUpdated = cms.EDProducer('PATElectronUpdater',
  computeMiniIso = cms.bool(False),
  pfCandsForMiniIso = cms.InputTag('packedPFCandidates')
)
