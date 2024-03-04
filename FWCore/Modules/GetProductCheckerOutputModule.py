import FWCore.ParameterSet.Config as cms

def GetProductCheckerOutputModule(**kwargs):
  mod = cms.OutputModule('GetProductCheckerOutputModule',
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    ),
    verbose = cms.untracked.bool(False)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
