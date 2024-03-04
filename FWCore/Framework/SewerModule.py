import FWCore.ParameterSet.Config as cms

def SewerModule(**kwargs):
  mod = cms.OutputModule('SewerModule',
    name = cms.required.string,
    shouldPass = cms.required.int32,
    outputCommands = cms.untracked.vstring('drop *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
