import FWCore.ParameterSet.Config as cms

def SiStripChannelGainFromDBMiscalibrator(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripChannelGainFromDBMiscalibrator',
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
    printDebug = cms.untracked.uint32(1),
    record = cms.untracked.string('SiStripApvGainRcd'),
    gainType = cms.untracked.uint32(1),
    saveMaps = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
