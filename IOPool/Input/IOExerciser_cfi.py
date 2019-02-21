import FWCore.ParameterSet.Config as cms

IOExerciser = cms.OutputModule('IOExerciser',
  percentBranches = cms.untracked.uint32(100),
  selectionStrategy = cms.untracked.string('smallestFirst'),
  triggerFactor = cms.untracked.uint32(0),
  outputCommands = cms.untracked.vstring('keep *'),
  SelectEvents = cms.untracked.PSet()
)
