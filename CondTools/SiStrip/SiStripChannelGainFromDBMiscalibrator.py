import FWCore.ParameterSet.Config as cms

def SiStripChannelGainFromDBMiscalibrator(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripChannelGainFromDBMiscalibrator',
    params = cms.VPSet(
      cms.PSet()
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
