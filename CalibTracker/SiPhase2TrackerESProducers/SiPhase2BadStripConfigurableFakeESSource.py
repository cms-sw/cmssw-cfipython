import FWCore.ParameterSet.Config as cms

def SiPhase2BadStripConfigurableFakeESSource(*args, **kwargs):
  mod = cms.ESSource('SiPhase2BadStripConfigurableFakeESSource',
    seed = cms.uint32(1),
    printDebug = cms.untracked.bool(False),
    badComponentsFraction = cms.double(0.01),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
