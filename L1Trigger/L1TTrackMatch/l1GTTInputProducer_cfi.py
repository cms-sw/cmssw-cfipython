import FWCore.ParameterSet.Config as cms

l1GTTInputProducer = cms.EDProducer('L1GTTInputProducer',
  debug = cms.int32(0),
  l1TracksInputTag = cms.InputTag('TTTracksFromTrackletEmulation', 'Level1TTTracks'),
  outputCollectionName = cms.string('Level1TTTracksConverted'),
  mightGet = cms.optional.untracked.vstring
)
