import FWCore.ParameterSet.Config as cms

def PackedCandidateTrackValidator(*args, **kwargs):
  mod = cms.EDProducer('PackedCandidateTrackValidator',
    tracks = cms.untracked.InputTag('generalTracks'),
    vertices = cms.untracked.InputTag('offlinePrimaryVertices'),
    trackToPackedCandidateAssociation = cms.untracked.InputTag('packedPFCandidates'),
    rootFolder = cms.untracked.string('Tracking/PackedCandidate'),
    debug = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
