import FWCore.ParameterSet.Config as cms

def SiStripApvGainRescaler(**kwargs):
  mod = cms.EDAnalyzer('SiStripApvGainRescaler',
    Record = cms.string('SiStripApvGainRcd'),
    printDebug = cms.untracked.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
