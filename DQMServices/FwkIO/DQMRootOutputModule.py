import FWCore.ParameterSet.Config as cms

def DQMRootOutputModule(*args, **kwargs):
  mod = cms.OutputModule('DQMRootOutputModule',
    fileName = cms.required.untracked.string,
    logicalFileName = cms.untracked.string(''),
    filterOnRun = cms.untracked.uint32(0),
    splitLevel = cms.untracked.int32(99),
    outputCommands = cms.untracked.vstring(
      'drop *',
      'keep DQMToken_*_*_*'
    ),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    ),
    dataset = cms.untracked.PSet()
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
