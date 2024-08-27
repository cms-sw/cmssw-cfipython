import FWCore.ParameterSet.Config as cms

def HcalTimeSlewEP(**kwargs):
  mod = cms.ESSource('HcalTimeSlewEP',
    timeSlewParametersM2 = cms.VPSet(
      cms.PSet()
    ),
    timeSlewParametersM3 = cms.VPSet(
      cms.PSet()
    ),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
