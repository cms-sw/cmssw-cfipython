import FWCore.ParameterSet.Config as cms

def TestOutputWithGetterOfProducts(**kwargs):
  mod = cms.OutputModule('TestOutputWithGetterOfProducts',
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    ),
    expectedSum = cms.untracked.uint32(0)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
