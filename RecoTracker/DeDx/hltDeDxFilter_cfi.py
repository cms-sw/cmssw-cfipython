import FWCore.ParameterSet.Config as cms

hltDeDxFilter = cms.EDFilter('HLTDeDxFilter',
  saveTags = cms.bool(False),
  minDEDx = cms.double(0),
  minPT = cms.double(0),
  minNOM = cms.double(0),
  maxETA = cms.double(5.5),
  minNumValidHits = cms.double(0),
  maxNHitMissIn = cms.double(99),
  maxNHitMissMid = cms.double(99),
  maxRelTrkIsoDeltaRp3 = cms.double(-1),
  relTrkIsoDeltaRSize = cms.double(0.3),
  maxAssocCaloE = cms.double(-99),
  maxAssocCaloEDeltaRSize = cms.double(0.5),
  caloTowersTag = cms.InputTag('hltTowerMakerForAll'),
  inputTracksTag = cms.InputTag('hltL3Mouns'),
  inputDeDxTag = cms.InputTag('HLTdedxHarm2')
)
