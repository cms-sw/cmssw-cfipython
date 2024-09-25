import FWCore.ParameterSet.Config as cms

def TestOutputWithGetterOfProductsLimited(*args, **kwargs):
  mod = cms.OutputModule('TestOutputWithGetterOfProductsLimited',
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    ),
    concurrencyLimit = cms.untracked.uint32(1),
    expectedSum = cms.untracked.uint32(0)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
