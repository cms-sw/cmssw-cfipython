import FWCore.ParameterSet.Config as cms

ptMinTrackCountFilter = cms.EDFilter('PtMinTrackCountFilter',
  src = cms.InputTag('tracks'),
  minNumber = cms.uint32(1),
  ptMin = cms.double(0),
  cut = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)
