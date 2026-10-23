import FWCore.ParameterSet.Config as cms

def StudyTriggerHLT(*args, **kwargs):
  mod = cms.EDAnalyzer('StudyTriggerHLT',
    verbosity = cms.int32(0),
    labelMuon = cms.InputTag('muons', '', 'RECO'),
    labelTrack = cms.InputTag('generalTracks', '', 'RECO'),
    trackQuality = cms.string('highPurity'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
