import FWCore.ParameterSet.Config as cms

trackFromPackedCandidateProducer = cms.EDProducer('TrackFromPackedCandidateProducer',
  PFCandidates = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
