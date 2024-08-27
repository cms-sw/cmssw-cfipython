import FWCore.ParameterSet.Config as cms

def CSCGeometryOfStrips(**kwargs):
  mod = cms.EDAnalyzer('CSCGeometryOfStrips',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
