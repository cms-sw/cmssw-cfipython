import FWCore.ParameterSet.Config as cms

diMuonVertexMonitor = cms.EDProducer('DiMuonVertexMonitor',
  muonTracks = cms.InputTag('ALCARECOTkAlDiMuon'),
  vertices = cms.InputTag('offlinePrimaryVertices'),
  FolderName = cms.string('DiMuonVertexMonitor'),
  useClosestVertex = cms.bool(True),
  maxSVdist = cms.double(50),
  mightGet = cms.optional.untracked.vstring
)
