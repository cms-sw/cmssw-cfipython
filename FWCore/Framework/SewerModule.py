import FWCore.ParameterSet.Config as cms

def SewerModule(*args, **kwargs):
  mod = cms.OutputModule('SewerModule',
    name = cms.required.string,
    shouldPass = cms.required.int32,
    outputCommands = cms.untracked.vstring('drop *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
