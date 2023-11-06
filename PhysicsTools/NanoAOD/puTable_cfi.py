import FWCore.ParameterSet.Config as cms

puTable = cms.EDProducer('NPUTablesProducer',
  src = cms.InputTag('slimmedAddPileupInfo'),
  pvsrc = cms.InputTag('offlineSlimmedPrimaryVertices'),
  zbins = cms.vdouble(),
  savePtHatMax = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
