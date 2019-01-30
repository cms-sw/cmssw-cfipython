import FWCore.ParameterSet.Config as cms

hlt22HLTCountNumberOfObjectIN3edm4ViewIN4reco5TrackEEEE = cms.EDFilter('HLTCountNumberOfTrack',
  saveTags = cms.bool(False),
  src = cms.InputTag(''),
  MinN = cms.int32(0),
  MaxN = cms.int32(99999)
)
