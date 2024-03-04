import FWCore.ParameterSet.Config as cms

def TestOutputWithGetterOfProductsLimited(**kwargs):
  mod = cms.OutputModule('TestOutputWithGetterOfProductsLimited',
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    ),
    concurrencyLimit = cms.untracked.uint32(1),
    expectedSum = cms.untracked.uint32(0)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
