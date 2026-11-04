import FWCore.ParameterSet.Config as cms

def SiPhase2BadSensorsByHandBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPhase2BadSensorsByHandBuilder',
    SinceAppendMode = cms.required.bool,
    IOVMode = cms.required.string,
    Record = cms.required.string,
    doStoreOnDB = cms.required.bool,
    TimeFromEndRun = cms.untracked.bool(False),
    TimeFromStartOfRunRange = cms.untracked.bool(False),
    printDebug = cms.untracked.bool(False),
    badSensorListFile = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
