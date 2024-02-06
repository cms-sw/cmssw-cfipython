import FWCore.ParameterSet.Config as cms

trackMultiplicityFilter = cms.EDFilter('TrackMultiplicityFilter',
  trackInputTag = cms.untracked.InputTag('generalTracks'),
  cut = cms.untracked.string(''),
  nmin = cms.untracked.uint32(0),
  mightGet = cms.optional.untracked.vstring
)
