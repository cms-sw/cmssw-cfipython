import FWCore.ParameterSet.Config as cms

def TestGlobalOutput(*args, **kwargs):
  mod = cms.OutputModule('TestGlobalOutput',
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    ),
    verbose = cms.untracked.bool(True),
    expectedProcessesWithProcessBlockProducts = cms.untracked.vstring(),
    expectedWriteProcessBlockTransitions = cms.untracked.int32(-1)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
