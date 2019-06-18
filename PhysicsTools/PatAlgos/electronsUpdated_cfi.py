import FWCore.ParameterSet.Config as cms

electronsUpdated = cms.EDProducer('PATElectronUpdater',
  src = cms.required.InputTag,
  vertices = cms.required.InputTag,
  computeMiniIso = cms.bool(False),
  pfCandsForMiniIso = cms.InputTag('packedPFCandidates'),
  miniIsoParamsB = cms.optional.vdouble,
  miniIsoParamsE = cms.optional.vdouble,
  mightGet = cms.optional.untracked.vstring
)
