import FWCore.ParameterSet.Config as cms

hltHcalCalibTypeFilter = cms.EDFilter('HLTHcalCalibTypeFilter',
  InputTag = cms.InputTag('source'),
  CalibTypes = cms.vint32(
    1,
    2,
    3,
    4,
    5
  ),
  mightGet = cms.optional.untracked.vstring
)
