import FWCore.ParameterSet.Config as cms

def PCaloGeometryBuilder(**kwargs):
  mod = cms.EDAnalyzer('PCaloGeometryBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
