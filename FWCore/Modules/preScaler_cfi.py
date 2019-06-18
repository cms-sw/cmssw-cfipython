import FWCore.ParameterSet.Config as cms

preScaler = cms.EDFilter('Prescaler',
  prescaleFactor = cms.required.int32,
  prescaleOffset = cms.required.int32,
  mightGet = cms.optional.untracked.vstring
)
