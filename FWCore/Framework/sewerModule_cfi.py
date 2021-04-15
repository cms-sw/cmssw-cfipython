import FWCore.ParameterSet.Config as cms

sewerModule = cms.OutputModule('SewerModule',
  name = cms.required.string,
  shouldPass = cms.required.int32,
  outputCommands = cms.untracked.vstring('drop *'),
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.optional.vstring
  )
)
