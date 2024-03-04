import FWCore.ParameterSet.Config as cms

def AsciiOutputModule(**kwargs):
  mod = cms.OutputModule('AsciiOutputModule',
    prescale = cms.untracked.uint32(1),
    verbosity = cms.untracked.uint32(1),
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
