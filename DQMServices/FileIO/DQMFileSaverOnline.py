import FWCore.ParameterSet.Config as cms

def DQMFileSaverOnline(**kwargs):
  mod = cms.EDAnalyzer('DQMFileSaverOnline',
    backupLumiCount = cms.untracked.int32(10),
    keepBackupLumi = cms.untracked.bool(False),
    tag = cms.untracked.string('UNKNOWN'),
    producer = cms.untracked.string('DQM'),
    referenceHandling = cms.untracked.string('all'),
    referenceRequireStatus = cms.untracked.int32(100),
    path = cms.untracked.string('./'),
    runNumber = cms.untracked.int32(111),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
