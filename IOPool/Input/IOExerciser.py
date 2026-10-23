import FWCore.ParameterSet.Config as cms

def IOExerciser(*args, **kwargs):
  mod = cms.OutputModule('IOExerciser',
    percentBranches = cms.untracked.uint32(100),
    selectionStrategy = cms.untracked.string('smallestFirst'),
    triggerFactor = cms.untracked.uint32(0),
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
