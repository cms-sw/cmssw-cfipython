import FWCore.ParameterSet.Config as cms

def edmtest_TableTestOutputModule(*args, **kwargs):
  mod = cms.OutputModule('edmtest::TableTestOutputModule',
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
