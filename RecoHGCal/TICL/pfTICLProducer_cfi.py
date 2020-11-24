import FWCore.ParameterSet.Config as cms

pfTICLProducer = cms.EDProducer('PFTICLProducer',
  ticlCandidateSrc = cms.InputTag('ticlTrackstersMerge'),
  mightGet = cms.optional.untracked.vstring
)
