import FWCore.ParameterSet.Config as cms

def HcalGeometryDump(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalGeometryDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
