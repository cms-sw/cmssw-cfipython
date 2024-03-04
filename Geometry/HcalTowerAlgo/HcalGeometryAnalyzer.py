import FWCore.ParameterSet.Config as cms

def HcalGeometryAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
