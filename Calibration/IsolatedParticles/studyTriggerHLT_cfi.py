import FWCore.ParameterSet.Config as cms

studyTriggerHLT = cms.EDAnalyzer('StudyTriggerHLT',
  verbosity = cms.int32(0),
  labelMuon = cms.InputTag('muons', '', 'RECO'),
  labelTrack = cms.InputTag('generalTracks', '', 'RECO'),
  trackQuality = cms.string('highPurity'),
  mightGet = cms.optional.untracked.vstring
)
