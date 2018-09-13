import FWCore.ParameterSet.Config as cms

hltBeamModeFilter = cms.EDFilter('HLTBeamModeFilter',
  saveTags = cms.bool(False),
  L1GtEvmReadoutRecordTag = cms.InputTag('gtEvmDigis'),
  AllowedBeamMode = cms.vuint32(11)
)
