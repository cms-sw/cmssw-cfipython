import FWCore.ParameterSet.Config as cms

def GEMGeometryValidate(**kwargs):
  mod = cms.EDAnalyzer('GEMGeometryValidate',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
