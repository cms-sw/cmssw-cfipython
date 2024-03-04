import FWCore.ParameterSet.Config as cms

def CSCGeometryValidate(**kwargs):
  mod = cms.EDAnalyzer('CSCGeometryValidate',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
