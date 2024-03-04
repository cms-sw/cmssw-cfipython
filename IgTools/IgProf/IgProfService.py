import FWCore.ParameterSet.Config as cms

def IgProfService(**kwargs):
  mod = cms.Service('IgProfService',
    reportEventInterval = cms.untracked.int32(1),
    reportFirstEvent = cms.untracked.int32(1),
    reportToFileAtPostBeginJob = cms.untracked.string(''),
    reportToFileAtPostBeginRun = cms.untracked.string(''),
    reportToFileAtPostBeginLumi = cms.untracked.string(''),
    reportToFileAtPreEvent = cms.untracked.string(''),
    reportToFileAtPostEvent = cms.untracked.string(''),
    reportModules = cms.untracked.vstring(),
    reportModuleTypes = cms.untracked.vstring(),
    reportToFileAtPreModuleEvent = cms.untracked.string(''),
    reportToFileAtPostModuleEvent = cms.untracked.string(''),
    reportToFileAtPostEndLumi = cms.untracked.string(''),
    reportToFileAtPreEndRun = cms.untracked.string(''),
    reportToFileAtPostEndRun = cms.untracked.string(''),
    reportToFileAtPreEndProcessBlock = cms.untracked.string(''),
    reportToFileAtPostEndProcessBlock = cms.untracked.string(''),
    reportToFileAtPreEndJob = cms.untracked.string(''),
    reportToFileAtPostEndJob = cms.untracked.string(''),
    reportToFileAtPostOpenFile = cms.untracked.string(''),
    reportToFileAtPostCloseFile = cms.untracked.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
