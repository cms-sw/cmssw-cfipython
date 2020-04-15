import FWCore.ParameterSet.Config as cms

pfTICLProducer = cms.EDProducer('PFTICLProducer',
  ticlCandidateSrc = cms.InputTag('ticlCandidateFromTracksters'),
  mightGet = cms.optional.untracked.vstring
)
