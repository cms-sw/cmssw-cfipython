import FWCore.ParameterSet.Config as cms

pfTICL = cms.EDProducer('PFTICLProducer',
  ticlCandidateSrc = cms.InputTag('ticlCandidateFromTracksters'),
  mightGet = cms.optional.untracked.vstring
)
