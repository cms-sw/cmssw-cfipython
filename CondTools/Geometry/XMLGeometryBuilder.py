import FWCore.ParameterSet.Config as cms

def XMLGeometryBuilder(**kwargs):
  mod = cms.EDAnalyzer('XMLGeometryBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
