import FWCore.ParameterSet.Config as cms

jetVertexChecker = cms.EDFilter('JetVertexChecker',
  beamSpot = cms.InputTag('hltOnlineBeamSpot'),
  jetTracks = cms.InputTag('hltFastPVJetTracksAssociator'),
  minPtRatio = cms.double(0.1),
  minPt = cms.double(0),
  doFilter = cms.bool(False),
  maxNJetsToCheck = cms.int32(2),
  maxNjetsOutput = cms.int32(2),
  maxChi2 = cms.double(20),
  maxTrackPt = cms.double(20),
  newMethod = cms.bool(False),
  maxETA = cms.double(2.4),
  pvErr_x = cms.double(0.0015),
  pvErr_y = cms.double(0.0015),
  pvErr_z = cms.double(1.5)
)
