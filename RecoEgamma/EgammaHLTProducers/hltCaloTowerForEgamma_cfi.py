import FWCore.ParameterSet.Config as cms

hltCaloTowerForEgamma = cms.EDProducer('EgammaHLTCaloTowerProducer',
  towerCollection = cms.InputTag('hltRecoEcalCandidate'),
  L1IsoCand = cms.InputTag('hltTowerMakerForAll'),
  L1NonIsoCand = cms.InputTag('fixedGridRhoFastjetAllCalo'),
  useTowersInCone = cms.double(0.8),
  EtMin = cms.double(1),
  EMin = cms.double(1),
  mightGet = cms.optional.untracked.vstring
)
