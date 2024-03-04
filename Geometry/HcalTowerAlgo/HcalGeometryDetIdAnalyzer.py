import FWCore.ParameterSet.Config as cms

def HcalGeometryDetIdAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalGeometryDetIdAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
