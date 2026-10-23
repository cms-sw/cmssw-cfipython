import FWCore.ParameterSet.Config as cms

def SiStripApvGainRescaler(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripApvGainRescaler',
    Record = cms.string('SiStripApvGainRcd'),
    printDebug = cms.untracked.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
