import FWCore.ParameterSet.Config as cms

def HBHEDarkeningEP(**kwargs):
  mod = cms.ESSource('HBHEDarkeningEP',
    ieta_shift = cms.required.int32,
    drdA = cms.required.double,
    drdB = cms.required.double,
    dosemaps = cms.VPSet(
      cms.PSet()
    ),
    years = cms.VPSet(
      cms.PSet()
    ),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
