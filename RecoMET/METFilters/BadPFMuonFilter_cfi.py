import FWCore.ParameterSet.Config as cms

from .BadParticleFilter import BadParticleFilter

BadPFMuonFilter = BadParticleFilter(
  innerTrackRelErr = 1,
  minDzBestTrack = -1,
  PFCandidates = ('particleFlow'),
  filterType = 'BadPFMuon',
  segmentCompatibility = 0.3,
  minMuonPt = 100,
  algo = 14,
  taggingMode = False,
  vtx = ('offlinePrimaryVertices'),
  minMuonTrackRelErr = 2,
  maxDR = 0.001,
  muons = ('muons'),
  minPtDiffRel = 0
)
