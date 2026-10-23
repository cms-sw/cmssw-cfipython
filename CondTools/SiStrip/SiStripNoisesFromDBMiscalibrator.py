import FWCore.ParameterSet.Config as cms

def SiStripNoisesFromDBMiscalibrator(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripNoisesFromDBMiscalibrator',
    params = cms.VPSet(
      cms.PSet(),
      template = cms.PSetTemplate(
        partition = cms.string('Tracker'),
        doScale = cms.bool(True),
        doSmear = cms.bool(True),
        scaleFactor = cms.double(1),
        smearFactor = cms.double(1)
      )
    ),
    printDebug = cms.untracked.uint32(10),
    perDetIDdebug = cms.untracked.bool(False),
    fillDefaults = cms.untracked.bool(False),
    saveMaps = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
