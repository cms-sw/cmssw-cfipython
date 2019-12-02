import FWCore.ParameterSet.Config as cms

pfTICLProducer = cms.EDProducer('PFTICLProducer',
  ticlCandidateSrc = cms.InputTag('ticlCandidateFromTrackstersProducer'),
  mightGet = cms.optional.untracked.vstring
)
