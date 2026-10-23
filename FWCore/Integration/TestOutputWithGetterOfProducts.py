import FWCore.ParameterSet.Config as cms

def TestOutputWithGetterOfProducts(*args, **kwargs):
  mod = cms.OutputModule('TestOutputWithGetterOfProducts',
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    ),
    expectedSum = cms.untracked.uint32(0)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
