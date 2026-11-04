import FWCore.ParameterSet.Config as cms

def SiPhase2ITBadSensorsReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPhase2ITBadSensorsReader',
    printDebug = cms.untracked.bool(False),
    label = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
