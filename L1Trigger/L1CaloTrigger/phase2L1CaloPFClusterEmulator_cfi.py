import FWCore.ParameterSet.Config as cms

phase2L1CaloPFClusterEmulator = cms.EDProducer('Phase2L1CaloPFClusterEmulator',
  gctFullTowers = cms.InputTag('l1tPhase2L1CaloEGammaEmulator', 'GCTFullTowers'),
  mightGet = cms.optional.untracked.vstring
)
