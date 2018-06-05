import FWCore.ParameterSet.Config as cms

hltCaloTowerHtMhtProducer = cms.EDProducer('HLTCaloTowerHtMhtProducer',
  usePt = cms.bool(False),
  minPtTowerHt = cms.double(1),
  minPtTowerMht = cms.double(1),
  maxEtaTowerHt = cms.double(5),
  maxEtaTowerMht = cms.double(5),
  towersLabel = cms.InputTag('hltTowerMakerForAll')
)
