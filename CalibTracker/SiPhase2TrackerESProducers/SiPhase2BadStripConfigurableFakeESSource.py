import FWCore.ParameterSet.Config as cms

def SiPhase2BadStripConfigurableFakeESSource(**kwargs):
  mod = cms.ESSource('SiPhase2BadStripConfigurableFakeESSource',
    seed = cms.uint32(1),
    printDebug = cms.untracked.bool(False),
    badComponentsFraction = cms.double(0.01),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
