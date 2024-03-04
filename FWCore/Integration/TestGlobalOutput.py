import FWCore.ParameterSet.Config as cms

def TestGlobalOutput(**kwargs):
  mod = cms.OutputModule('TestGlobalOutput',
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    ),
    verbose = cms.untracked.bool(True),
    expectedProcessesWithProcessBlockProducts = cms.untracked.vstring(),
    expectedWriteProcessBlockTransitions = cms.untracked.int32(-1)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
