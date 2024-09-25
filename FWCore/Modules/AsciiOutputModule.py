import FWCore.ParameterSet.Config as cms

def AsciiOutputModule(*args, **kwargs):
  mod = cms.OutputModule('AsciiOutputModule',
    prescale = cms.untracked.uint32(1),
    verbosity = cms.untracked.uint32(1),
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
