import FWCore.ParameterSet.Config as cms

caloTowerConstituents = cms.ESProducer('CaloTowerConstituentsMapBuilder',
  MapFile = cms.untracked.string(''),
  MapAuto = cms.untracked.bool(False),
  SkipHE = cms.untracked.bool(False),
  appendToDataLabel = cms.string('')
)
