import FWCore.ParameterSet.Config as cms

def L1GTTInputProducer(**kwargs):
  mod = cms.EDProducer('L1GTTInputProducer',
    debug = cms.int32(0),
    l1TracksInputTag = cms.InputTag('TTTracksFromTrackletEmulation', 'Level1TTTracks'),
    outputCollectionName = cms.string('Level1TTTracksConverted'),
    setTrackWordBits = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
