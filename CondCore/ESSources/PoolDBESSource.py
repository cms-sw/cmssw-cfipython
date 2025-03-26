import FWCore.ParameterSet.Config as cms

def PoolDBESSource(*args, **kwargs):
  mod = cms.ESSource('PoolDBESSource',
    DBParameters = cms.PSet(
      authenticationPath = cms.untracked.string(''),
      authenticationSystem = cms.untracked.int32(0),
      security = cms.untracked.string(''),
      messageLevel = cms.untracked.int32(0),
      connectionTimeout = cms.untracked.int32(0)
    ),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string(''),
    snapshotTime = cms.string(''),
    frontierKey = cms.untracked.string(''),
    toGet = cms.VPSet(
      template = cms.PSetTemplate(
        record = cms.string(''),
        tag = cms.string(''),
        snapshotTime = cms.string(''),
        connect = cms.string(''),
        refreshTime = cms.uint64(18446744073709551615),
        label = cms.untracked.string('')
      )
    ),
    JsonDumpFileName = cms.untracked.string(''),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
