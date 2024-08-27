import FWCore.ParameterSet.Config as cms

def SiStripDetVOffPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripDetVOffPrinter',
    conditionDatabase = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    tagName = cms.string('SiStripDetVOff_1hourDelay_v1_Validation'),
    startTime = cms.string('2002-01-20 23:59:59.000'),
    endTime = cms.string('2002-01-20 23:59:59.000'),
    output = cms.string('PerModuleSummary.txt'),
    connect = cms.string(''),
    DBParameters = cms.PSet(
      authenticationPath = cms.untracked.string(''),
      authenticationSystem = cms.untracked.int32(0),
      security = cms.untracked.string(''),
      messageLevel = cms.untracked.int32(0)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
