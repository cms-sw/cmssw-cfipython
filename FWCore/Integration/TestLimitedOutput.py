import FWCore.ParameterSet.Config as cms

def TestLimitedOutput(**kwargs):
  mod = cms.OutputModule('TestLimitedOutput',
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    ),
    concurrencyLimit = cms.untracked.uint32(1),
    verbose = cms.untracked.bool(True),
    expectedProcessesWithProcessBlockProducts = cms.untracked.vstring(),
    expectedWriteProcessBlockTransitions = cms.untracked.int32(-1)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
