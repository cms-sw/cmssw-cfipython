import FWCore.ParameterSet.Config as cms

def HcalDDDGeometryAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalDDDGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
