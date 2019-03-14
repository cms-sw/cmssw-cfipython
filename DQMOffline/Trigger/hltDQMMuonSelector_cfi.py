import FWCore.ParameterSet.Config as cms

hltDQMMuonSelector = cms.EDProducer('HLTDQMMuonSelector',
  objs = cms.InputTag('muons'),
  vertices = cms.InputTag('offlinePrimaryVertices'),
  selection = cms.string('et > 5'),
  muonSelectionType = cms.string('tight')
)
