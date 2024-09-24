import FWCore.ParameterSet.Config as cms

def InitRootHandlers(*args, **kwargs):
  mod = cms.Service('InitRootHandlers',
    UnloadRootSigHandler = cms.untracked.bool(False),
    ResetRootErrHandler = cms.untracked.bool(True),
    AutoLibraryLoader = cms.untracked.bool(True),
    AutoClassParser = cms.untracked.bool(True),
    LoadAllDictionaries = cms.untracked.bool(False),
    EnableIMT = cms.untracked.bool(True),
    AbortOnSignal = cms.untracked.bool(True),
    InteractiveDebug = cms.untracked.bool(False),
    DebugLevel = cms.untracked.int32(0),
    StackTracePauseTime = cms.untracked.int32(300)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod