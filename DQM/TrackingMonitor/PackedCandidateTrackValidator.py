import FWCore.ParameterSet.Config as cms

def PackedCandidateTrackValidator(**kwargs):
  mod = cms.EDProducer('PackedCandidateTrackValidator',
    tracks = cms.untracked.InputTag('generalTracks'),
    vertices = cms.untracked.InputTag('offlinePrimaryVertices'),
    trackToPackedCandidateAssociation = cms.untracked.InputTag('packedPFCandidates'),
    rootFolder = cms.untracked.string('Tracking/PackedCandidate'),
    debug = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
