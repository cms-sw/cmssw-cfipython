import FWCore.ParameterSet.Config as cms

alcaHOCalibProducer = cms.EDProducer('AlCaHOCalibProducer',
  hbheInput = cms.InputTag('hbhereco'),
  hotime = cms.untracked.bool(False),
  hbinfo = cms.untracked.bool(False),
  sigma = cms.untracked.double(1),
  plotOccupancy = cms.untracked.bool(False),
  CosmicData = cms.untracked.bool(False),
  hoInput = cms.InputTag('horeco'),
  towerInput = cms.InputTag('towerMaker'),
  RootFileName = cms.untracked.string('test.root'),
  m_scale = cms.untracked.double(4),
  debug = cms.untracked.bool(False),
  muons = cms.untracked.InputTag('muons'),
  vertexTags = cms.InputTag('offlinePrimaryVertices'),
  lumiTags = cms.InputTag('scalersRawToDigi'),
  metadata = cms.InputTag('onlineMetaDataDigis'),
  mightGet = cms.optional.untracked.vstring
)
