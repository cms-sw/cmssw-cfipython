import FWCore.ParameterSet.Config as cms

def HcalTimeSlewEP(*args, **kwargs):
  mod = cms.ESSource('HcalTimeSlewEP',
    timeSlewParametersM2 = cms.VPSet(
      cms.PSet()
    ),
    timeSlewParametersM3 = cms.VPSet(
      cms.PSet()
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
