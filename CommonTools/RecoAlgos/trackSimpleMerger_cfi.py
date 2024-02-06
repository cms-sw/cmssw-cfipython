import FWCore.ParameterSet.Config as cms

trackSimpleMerger = cms.EDProducer('TrackSimpleMerger',
  src = cms.VInputTag(
    'collection1',
    'collection2'
  ),
  mightGet = cms.optional.untracked.vstring
)
