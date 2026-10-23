import FWCore.ParameterSet.Config as cms

def GetProductCheckerOutputModule(*args, **kwargs):
  mod = cms.OutputModule('GetProductCheckerOutputModule',
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    ),
    crosscheck = cms.untracked.vstring(),
    verbose = cms.untracked.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
