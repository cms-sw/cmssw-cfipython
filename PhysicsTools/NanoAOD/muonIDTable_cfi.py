import FWCore.ParameterSet.Config as cms

muonIDTable = cms.EDProducer('MuonIDTableProducer',
  vertices = cms.InputTag('offlineSlimmedPrimaryVertices')
)
