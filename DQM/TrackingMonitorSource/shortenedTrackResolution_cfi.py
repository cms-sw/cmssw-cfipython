import FWCore.ParameterSet.Config as cms

shortenedTrackResolution = cms.EDProducer('ShortenedTrackResolution',
  folderName = cms.untracked.string('TrackRefitting'),
  hitsRemainInput = cms.untracked.vstring(),
  minTracksEtaInput = cms.untracked.double(0),
  maxTracksEtaInput = cms.untracked.double(2.2),
  minTracksPtInput = cms.untracked.double(15),
  maxTracksPtInput = cms.untracked.double(99999.9),
  maxDrInput = cms.untracked.double(0.01),
  tracksInputTag = cms.untracked.InputTag('generalTracks', '', 'DQM'),
  tracksRerecoInputTag = cms.untracked.VInputTag(),
  mightGet = cms.optional.untracked.vstring
)
