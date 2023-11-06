import FWCore.ParameterSet.Config as cms

siPhase2BadStripConfigurableFakeESSource = cms.ESSource('SiPhase2BadStripConfigurableFakeESSource',
  seed = cms.uint32(1),
  printDebug = cms.untracked.bool(False),
  badComponentsFraction = cms.double(0.01),
  appendToDataLabel = cms.string('')
)
