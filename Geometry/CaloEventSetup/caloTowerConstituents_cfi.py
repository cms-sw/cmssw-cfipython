import FWCore.ParameterSet.Config as cms

caloTowerConstituents = cms.ESProducer('CaloTowerConstituentsMapBuilder',
  MapFile = cms.untracked.string(''),
  appendToDataLabel = cms.string('')
)
