import FWCore.ParameterSet.Config as cms

def PPSGeometryBuilder(**kwargs):
  mod = cms.EDAnalyzer('PPSGeometryBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
