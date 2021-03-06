import FWCore.ParameterSet.Config as cms

magneticFieldFilter = cms.EDFilter('MagneticFieldFilter',
  magneticField = cms.untracked.int32(38),
  mightGet = cms.optional.untracked.vstring
)
