import FWCore.ParameterSet.Config as cms

BadPFMuonFilter = cms.EDFilter('BadParticleFilter',
  innerTrackRelErr = cms.double(1),
  minDzBestTrack = cms.double(-1),
  PFCandidates = cms.InputTag('particleFlow'),
  filterType = cms.string('BadPFMuon'),
  segmentCompatibility = cms.double(0.3),
  minMuonPt = cms.double(100),
  algo = cms.int32(14),
  taggingMode = cms.bool(False),
  vtx = cms.InputTag('offlinePrimaryVertices'),
  minMuonTrackRelErr = cms.double(2),
  maxDR = cms.double(0.001),
  muons = cms.InputTag('muons'),
  minPtDiffRel = cms.double(0),
  mightGet = cms.optional.untracked.vstring
)
