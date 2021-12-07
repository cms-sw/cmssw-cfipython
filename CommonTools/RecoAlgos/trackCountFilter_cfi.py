import FWCore.ParameterSet.Config as cms

trackCountFilter = cms.EDFilter('TrackCountFilter',
  src = cms.InputTag(''),
  minNumber = cms.uint32(0),
  mightGet = cms.optional.untracked.vstring
)
