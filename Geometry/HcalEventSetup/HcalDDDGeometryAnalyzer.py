import FWCore.ParameterSet.Config as cms

def HcalDDDGeometryAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalDDDGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
