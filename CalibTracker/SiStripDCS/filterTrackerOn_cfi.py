import FWCore.ParameterSet.Config as cms

filterTrackerOn = cms.EDFilter('FilterTrackerOn',
  MinModulesWithHVoff = cms.untracked.int32(0),
  mightGet = cms.optional.untracked.vstring
)
