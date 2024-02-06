import FWCore.ParameterSet.Config as cms

ptMaxTrackCountFilter = cms.EDFilter('PtMaxTrackCountFilter',
  src = cms.InputTag('tracks'),
  minNumber = cms.uint32(1),
  ptMax = cms.double(999),
  cut = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)
