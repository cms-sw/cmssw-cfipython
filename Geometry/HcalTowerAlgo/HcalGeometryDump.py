import FWCore.ParameterSet.Config as cms

def HcalGeometryDump(**kwargs):
  mod = cms.EDAnalyzer('HcalGeometryDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
