import FWCore.ParameterSet.Config as cms

def SiStripQualityStatistics(*args, **kwargs):
  mod = cms.EDProducer('SiStripQualityStatistics',
    TkMapFileName = cms.untracked.string(''),
    SaveTkHistoMap = cms.untracked.bool(True),
    file = cms.untracked.FileInPath('CalibTracker/SiStripCommon/data/SiStripDetInfo.dat'),
    StripQualityLabel = cms.string(''),
    BadComponentsFromFedErrors = cms.PSet(
      Add = cms.bool(False),
      Cutoff = cms.double(0.8),
      LegacyDQMFile = cms.string(''),
      FileRunNumber = cms.uint32(4294967295)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
