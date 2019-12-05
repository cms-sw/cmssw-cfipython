import FWCore.ParameterSet.Config as cms

EnableFloatingPointExceptions = cms.Service('EnableFloatingPointExceptions',
  reportSettings = cms.untracked.bool(False),
  setPrecisionDouble = cms.untracked.bool(True),
  moduleNames = cms.untracked.vstring()
)
